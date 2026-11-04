from brain_of_doctor import brain_of_the_doctor
from voice_of_doctor import speak
from voice_of_patient import transcribe_audio
import gradio as gr


def process_inputs(audio_filepath, image_filepath, video_filepath):

    # Convert patient's audio into text
    if audio_filepath:
        patient_text = transcribe_audio(audio_filepath)
    else:
        patient_text = ""

    # Send patient's text and image/video to Gemini
    doctor_text = brain_of_the_doctor(
        patient_text=patient_text,
        image_filepath=image_filepath,
        video_filepath=video_filepath,
    )

    # Convert doctor's text response into audio
    doctor_audio = speak(doctor_text, play_audio=False)

    # Return all outputs to Gradio
    return patient_text, doctor_text, str(doctor_audio)


# Logic + UI
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(
            sources=["microphone", "upload"], type="filepath", label="Patient Voice"
        ),
        gr.Image(type="filepath", label="Patient Image"),
        gr.Video(label="Patient Video"),
    ],
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio(label="Doctor's Voice"),
    ],
    title="AI Doctor with Vision and Voice",
)

iface.launch()
