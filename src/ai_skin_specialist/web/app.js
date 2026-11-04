const byId = (id) => document.getElementById(id);
const files = { audio: null, image: null, video: null };
const history = [];
let mediaRecorder = null;
let recordingChunks = [];
let recordingStream = null;
let recordingStarted = 0;
let recordingInterval = null;
let discardRecording = false;
let responseAudioUrl = null;

function showView(name) {
  document.querySelectorAll(".view").forEach((view) => view.classList.remove("active"));
  byId(`view-${name}`).classList.add("active");
  document.querySelectorAll(".nav-link").forEach((button) => {
    button.classList.toggle("active", button.dataset.view === name);
  });
  const titles = {
    consultation: "New consultation",
    history: "Consultation history",
    guide: "Skin health guide",
    settings: "Settings",
  };
  byId("page-title").textContent = titles[name];
  document.body.classList.remove("nav-open");
  if (name === "history") renderHistory();
}

document.querySelectorAll("[data-view]").forEach((button) => {
  button.addEventListener("click", () => {
    const name = button.dataset.view;
    if (name === "consultation" && button.matches(".brand")) resetConsultation();
    showView(name);
  });
});

document.querySelector(".mobile-menu").addEventListener("click", () => {
  document.body.classList.toggle("nav-open");
});

document.querySelectorAll(".prompt-chip").forEach((button) => {
  button.addEventListener("click", () => {
    byId("concern").value = `${byId("concern").value.trim()}${byId("concern").value.trim() ? " " : ""}${button.textContent}. `;
    byId("concern").focus();
  });
});

document.querySelectorAll(".suggested-prompt").forEach((button) => {
  button.addEventListener("click", () => {
    const prompt = button.childNodes[0]?.textContent.trim() || button.textContent.trim();
    byId("concern").value = prompt.replace(/[“”]/g, "");
    byId("concern").focus();
    byId("concern").scrollIntoView({ behavior: "smooth", block: "center" });
  });
});

function chooseFile(kind, inputId, previewId) {
  const input = byId(inputId);
  input.addEventListener("change", () => {
    const file = input.files?.[0] ?? null;
    files[kind] = file;
    if (kind === "audio") {
      byId("audio-name").textContent = file ? `Selected: ${file.name}` : "";
      byId("audio-name").classList.toggle("hidden", !file);
      byId("remove-audio-button").disabled = !file;
      return;
    }

    const preview = byId(previewId);
    preview.replaceChildren();
    preview.classList.toggle("hidden", !file);
    if (!file) return;

    const media = document.createElement(kind === "image" ? "img" : "video");
    media.src = URL.createObjectURL(file);
    if (kind === "video") {
      media.muted = true;
      media.playsInline = true;
    }
    const name = document.createElement("span");
    name.className = "preview-name";
    name.textContent = file.name;
    const remove = document.createElement("button");
    remove.type = "button";
    remove.className = "remove-file";
    remove.textContent = "Remove";
    remove.addEventListener("click", () => {
      URL.revokeObjectURL(media.src);
      input.value = "";
      files[kind] = null;
      preview.replaceChildren();
      preview.classList.add("hidden");
    });
    preview.append(media, name, remove);
  });
}

chooseFile("audio", "audio-file");
chooseFile("image", "image-file", "image-preview");
chooseFile("video", "video-file", "video-preview");

byId("record-button").addEventListener("click", async () => {
  if (mediaRecorder?.state === "recording") {
    mediaRecorder.stop();
    return;
  }
  if (!navigator.mediaDevices?.getUserMedia || !window.MediaRecorder) {
    setError("Voice recording is not supported by this browser. You can upload an audio recording instead.");
    return;
  }
  try {
    recordingStream = await navigator.mediaDevices.getUserMedia({ audio: true });
    recordingChunks = [];
    mediaRecorder = new MediaRecorder(recordingStream);
    mediaRecorder.addEventListener("dataavailable", (event) => {
      if (event.data.size) recordingChunks.push(event.data);
    });
    mediaRecorder.addEventListener("stop", () => {
      if (discardRecording) {
        discardRecording = false;
        recordingStream?.getTracks().forEach((track) => track.stop());
        recordingStream = null;
        byId("record-button").classList.remove("recording");
        byId("record-button").setAttribute("aria-label", "Start recording");
        clearInterval(recordingInterval);
        return;
      }
      const blob = new Blob(recordingChunks, { type: mediaRecorder.mimeType || "audio/webm" });
      files.audio = new File([blob], "voice-note.webm", { type: blob.type });
      byId("audio-file").value = "";
      byId("audio-name").textContent = "Recorded voice note is ready";
      byId("audio-name").classList.remove("hidden");
      byId("remove-audio-button").disabled = false;
      recordingStream?.getTracks().forEach((track) => track.stop());
      recordingStream = null;
      byId("record-button").classList.remove("recording");
      byId("record-button").setAttribute("aria-label", "Start recording");
      byId("recording-status").textContent = "Recording ready";
      clearInterval(recordingInterval);
    });
    mediaRecorder.start();
    recordingStarted = Date.now();
    byId("record-button").classList.add("recording");
    byId("record-button").setAttribute("aria-label", "Stop recording");
    byId("recording-status").textContent = "Listening…";
    byId("remove-audio-button").disabled = false;
    updateRecordingTime();
    recordingInterval = setInterval(updateRecordingTime, 250);
    setTimeout(() => {
      if (mediaRecorder?.state === "recording") mediaRecorder.stop();
    }, 60_000);
    clearError();
  } catch (error) {
    setError(error.name === "NotAllowedError"
      ? "Microphone access was denied. Allow microphone access or upload an audio recording."
      : `Could not start recording: ${error.message}`);
  }
});

function updateRecordingTime() {
  const seconds = Math.min(60, Math.floor((Date.now() - recordingStarted) / 1000));
  byId("recording-time").textContent = `${String(Math.floor(seconds / 60)).padStart(2, "0")}:${String(seconds % 60).padStart(2, "0")}`;
}

byId("analyze-button").addEventListener("click", submitConsultation);
byId("remove-audio-button").addEventListener("click", removeAudioNote);

function removeAudioNote() {
  if (mediaRecorder?.state === "recording") {
    discardRecording = true;
    mediaRecorder.stop();
  }
  recordingStream?.getTracks().forEach((track) => track.stop());
  recordingStream = null;
  files.audio = null;
  byId("audio-file").value = "";
  byId("audio-name").textContent = "";
  byId("audio-name").classList.add("hidden");
  byId("remove-audio-button").disabled = true;
  byId("recording-time").textContent = "00:00";
  byId("recording-status").textContent = "Ready to record";
  byId("record-button").classList.remove("recording");
  byId("record-button").setAttribute("aria-label", "Start recording");
  clearInterval(recordingInterval);
}

async function submitConsultation() {
  const concern = byId("concern").value.trim();
  if (mediaRecorder?.state === "recording") {
    setError("Stop the voice recording before requesting guidance.");
    return;
  }
  if (!concern && !files.audio && !files.image && !files.video) {
    setError("Describe your concern or add an audio recording, image, or video.");
    byId("concern").focus();
    return;
  }

  clearError();
  byId("assistant-welcome").classList.add("hidden");
  byId("assistant-results").classList.add("hidden");
  byId("assistant-loading").classList.remove("hidden");
  byId("analyze-button").disabled = true;
  byId("analyze-button").innerHTML = '<span class="loader small-loader"></span>Preparing guidance…';

  const body = new FormData();
  body.append("concern", concern);
  Object.entries(files).forEach(([kind, file]) => {
    if (file) body.append(kind, file);
  });

  try {
    const response = await fetch("/api/analyze", { method: "POST", body });
    let result;
    try {
      result = await response.json();
    } catch {
      throw new Error(`Consultation failed (${response.status}). Please try again.`);
    }
    if (!response.ok) throw new Error(result.detail || `The request failed (${response.status}).`);

    byId("result-transcript").textContent = result.transcript || "No spoken description was provided.";
    byId("result-response").textContent = result.response;
    if (result.audio) {
      const bytes = Uint8Array.from(atob(result.audio), (character) => character.charCodeAt(0));
      const blob = new Blob([bytes], { type: result.audio_mime || "audio/mpeg" });
      if (responseAudioUrl) URL.revokeObjectURL(responseAudioUrl);
      responseAudioUrl = URL.createObjectURL(blob);
      byId("response-audio").src = responseAudioUrl;
      byId("audio-player-wrap").classList.remove("hidden");
      byId("audio-unavailable").classList.add("hidden");
    } else {
      byId("response-audio").removeAttribute("src");
      byId("audio-player-wrap").classList.add("hidden");
      byId("audio-unavailable").classList.remove("hidden");
    }
    history.unshift({ date: new Date(), concern: concern || result.transcript, response: result.response });
    byId("assistant-loading").classList.add("hidden");
    byId("assistant-results").classList.remove("hidden");
  } catch (error) {
    byId("assistant-loading").classList.add("hidden");
    byId("assistant-welcome").classList.remove("hidden");
    setError(error.message || "The consultation could not be completed. Please try again.");
  } finally {
    byId("analyze-button").disabled = false;
    byId("analyze-button").innerHTML = '<span class="material-symbols-outlined">auto_awesome</span>Get guidance<span class="material-symbols-outlined trailing">arrow_forward</span>';
  }
}

byId("playback-speed").addEventListener("change", (event) => {
  byId("response-audio").playbackRate = Number(event.target.value);
});
byId("new-consultation-button").addEventListener("click", resetConsultation);

function resetConsultation() {
  byId("concern").value = "";
  ["audio", "image", "video"].forEach((kind) => { files[kind] = null; });
  ["audio-file", "image-file", "video-file"].forEach((id) => { byId(id).value = ""; });
  byId("audio-name").textContent = "";
  byId("audio-name").classList.add("hidden");
  byId("remove-audio-button").disabled = true;
  ["image-preview", "video-preview"].forEach((id) => {
    const preview = byId(id);
    preview.querySelectorAll("img, video").forEach((media) => URL.revokeObjectURL(media.src));
    preview.replaceChildren();
    preview.classList.add("hidden");
  });
  byId("response-audio").pause();
  byId("response-audio").removeAttribute("src");
  if (responseAudioUrl) URL.revokeObjectURL(responseAudioUrl);
  responseAudioUrl = null;
  byId("assistant-results").classList.add("hidden");
  byId("audio-unavailable").classList.add("hidden");
  byId("assistant-loading").classList.add("hidden");
  byId("assistant-welcome").classList.remove("hidden");
  byId("recording-time").textContent = "00:00";
  byId("recording-status").textContent = "Ready to record";
  clearError();
  showView("consultation");
}

function setError(message) {
  byId("error-message").textContent = message;
  byId("error-message").classList.remove("hidden");
}
function clearError() {
  byId("error-message").textContent = "";
  byId("error-message").classList.add("hidden");
}

function renderHistory() {
  const list = byId("history-list");
  list.replaceChildren();
  if (!history.length) {
    const empty = document.createElement("div");
    empty.className = "empty-history";
    empty.textContent = "No consultations yet. Completed consultations appear here for this page session only.";
    list.append(empty);
    return;
  }
  history.forEach((entry) => {
    const card = document.createElement("article");
    card.className = "history-item";
    const date = document.createElement("time");
    date.dateTime = entry.date.toISOString();
    date.textContent = entry.date.toLocaleString();
    const concern = document.createElement("p");
    concern.textContent = entry.concern || "Voice or media consultation";
    const response = document.createElement("p");
    response.textContent = entry.response;
    card.append(date, concern, response);
    list.append(card);
  });
}

async function loadStatus() {
  try {
    const response = await fetch("/api/status");
    if (!response.ok) throw new Error("Status is unavailable.");
    const services = await response.json();
    setServiceStatus("analysis-status", services.analysis, "Gemini");
    setServiceStatus("speech-status", services.speech, "Deepgram");
  } catch {
    setServiceStatus("analysis-status", false, "Unavailable");
    setServiceStatus("speech-status", false, "Unavailable");
  }
}

function setServiceStatus(id, ready, service) {
  const element = byId(id);
  element.textContent = ready ? `${service} ready` : `${service} not configured`;
  element.classList.toggle("ready", ready);
  element.classList.toggle("unavailable", !ready);
}

loadStatus();
