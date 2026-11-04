---
name: Derma AI Design System
colors:
  surface: '#f0fcf5'
  surface-dim: '#d1ddd6'
  surface-bright: '#f0fcf5'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#ebf6f0'
  surface-container: '#e5f1ea'
  surface-container-high: '#dfebe4'
  surface-container-highest: '#dae5df'
  on-surface: '#131e1a'
  on-surface-variant: '#414846'
  inverse-surface: '#28332e'
  inverse-on-surface: '#e8f4ed'
  outline: '#717976'
  outline-variant: '#c0c8c5'
  surface-tint: '#40655c'
  primary: '#002720'
  on-primary: '#ffffff'
  primary-container: '#173d35'
  on-primary-container: '#81a89d'
  inverse-primary: '#a7cfc3'
  secondary: '#516258'
  on-secondary: '#ffffff'
  secondary-container: '#d1e4d7'
  on-secondary-container: '#55675c'
  tertiary: '#371a00'
  on-tertiary: '#ffffff'
  tertiary-container: '#562c00'
  on-tertiary-container: '#e48b33'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#c2ebdf'
  primary-fixed-dim: '#a7cfc3'
  on-primary-fixed: '#00201a'
  on-primary-fixed-variant: '#284d45'
  secondary-fixed: '#d4e7d9'
  secondary-fixed-dim: '#b8cbbe'
  on-secondary-fixed: '#0f1f16'
  on-secondary-fixed-variant: '#3a4b40'
  tertiary-fixed: '#ffdcc2'
  tertiary-fixed-dim: '#ffb77a'
  on-tertiary-fixed: '#2e1500'
  on-tertiary-fixed-variant: '#6d3a00'
  background: '#f0fcf5'
  on-background: '#131e1a'
  surface-variant: '#dae5df'
typography:
  display-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 3.5rem
    fontWeight: '500'
    lineHeight: 4.25rem
    letterSpacing: -0.03em
  display-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 2.25rem
    fontWeight: '500'
    lineHeight: 2.75rem
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 2.25rem
    fontWeight: '500'
    lineHeight: 2.875rem
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 1.75rem
    fontWeight: '500'
    lineHeight: 2.25rem
    letterSpacing: -0.015em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 1.5rem
    fontWeight: '500'
    lineHeight: 2rem
    letterSpacing: -0.015em
  headline-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 1.25rem
    fontWeight: '500'
    lineHeight: 1.75rem
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 1.125rem
    fontWeight: '400'
    lineHeight: 1.75rem
    letterSpacing: -0.005em
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 1rem
    fontWeight: '400'
    lineHeight: 1.625rem
    letterSpacing: 0em
  body-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 0.875rem
    fontWeight: '400'
    lineHeight: 1.375rem
    letterSpacing: 0em
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 0.875rem
    fontWeight: '500'
    lineHeight: 1.25rem
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 0.75rem
    fontWeight: '600'
    lineHeight: 1rem
    letterSpacing: 0.04em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1.5rem
  gutter-desktop: 2rem
  margin: 1rem
  margin-tablet: 2rem
  margin-desktop: 4rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
---

## Brand & Style

This design system embodies clinical precision balanced with organic tranquility. It is crafted for patients and clinicians navigating intelligent dermatological analysis, requiring an atmosphere that projects scientific authority, discretion, and calm reassurance. 

The aesthetic is anchored in **Warm Organic Minimalism**—a synthesis of high-end editorial clarity, medical trustworthiness, and tactile softness. It avoids cold, clinical starkness in favor of warm off-white canvases, balanced botanical greens, and restrained hairline framing. Interactions must feel serene, deliberate, and whisper-quiet, instilling confidence through generous spatial breathing room, refined typographic cadence, and tactile micro-interactions.

## Colors

The palette derives its core strength from restorative biophilic tones and quiet neutrals.

- **Background & Canvas**: Surface foundation is grounded in `#F8F8F5` (Warm Off-White), rejecting stark synthetic whites to soothe visual fatigue. Elevated cards transition to pure `#FFFFFF`.
- **Primary Brand**: `#173D35` (Deep Forest Green) commands primary calls-to-action, active indicators, and high-emphasis brand anchor points.
- **Interactive Shift**: `#102B25` (Deep Spruce) provides weighted depth for active/hover states on primary elements.
- **Accents & Subtle Infusions**: `#A9BCAF` (Muted Sage) provides serene highlights, active waveform ripples, and secondary focal emphasis. Soft tinted surfaces (`#EBF1ED` and `#F1F5F2`) serve as resting grounds for tags, pill badges, and input fills.
- **Typography & Structure**: `#252B29` (Dark Charcoal) offers high-contrast legibility for titles without the harshness of pure black; `#4F5A55` handles clinical body copy and secondary metadata.
- **Borders & Dividers**: Crisp, hairline boundaries are established strictly with `#E3E8E4` and `#E9ECE9`.
- **Feedback & Diagnostics**: `#D9822B` (Gentle Amber) signals clinical observations requiring attention; `#D45D5D` (Soft Rose) conveys diagnostic anomalies or validation warnings without inducing panic.

## Typography

The type system relies exclusively on **Plus Jakarta Sans**, chosen for its balanced geometric structure, humanist curvature, and contemporary clinical warmth. 

Headings reject heavy, aggressive weights; instead, they utilize medium (`500`) weights with slight negative letter tracking to retain an editorial, dignified character. Body copy prioritizes optical legibility with spacious line heights (`1.625rem` on 16px body), allowing lengthy medical histories and AI diagnostic explanations to be parsed effortlessly. Uppercase styles are strictly constrained to small category labels and telemetry headers, deployed with wide tracking (`+0.04em`) to establish visual order.

## Layout & Spacing

The layout is structured around an airy, adaptive 12-column grid designed for focused clinical evaluation. 

- **Layout Philosophy**: The design system relies on a fluid grid bounded by a max-width container (`1440px`) to prevent sprawling text tracks and maintain scannability.
- **Rhythm**: Spacing follows an intentional 8pt spatial cadence. Internal card paddings use generous values (`1.5rem` to `2rem`) to frame medical imaging, transcriptions, and telemetry charts.
- **Breakpoints & Adaptation**:
  - **Mobile (<768px)**: 4-column flow, `1rem` edge margins, stacked single-column diagnostic flows. Toolbars and primary interaction triggers dock gracefully to bottom sheets.
  - **Tablet (768px–1023px)**: 8-column layout, `2rem` edge margins, multi-pane side-by-side assessment setups.
  - **Desktop (≥1024px)**: 12-column layout, `4rem` outer canvas padding, persistent clinical context rails (e.g., patient background sidebars alongside diagnostic feeds).

## Elevation & Depth

Spatial layering relies on flat, crisp surface separation backed by ultra-diffused, ambient shadowing. Surfaces avoid heavy drop shadows, simulating soft directional light falling across clean architectural paper.

- **Surface Levels**:
  - **Level 0 (Canvas)**: `#F8F8F5` background, baseline plain.
  - **Level 1 (Cards & Modules)**: Pure `#FFFFFF` surfaces bounded by a hairline 1px border (`#E3E8E4`). Shadows are subtle: `0 1px 3px rgba(23, 61, 53, 0.03), 0 4px 12px rgba(23, 61, 53, 0.02)`.
  - **Level 2 (Dropdowns, Floating Overlays, Controls)**: Pure `#FFFFFF` with expanded ambient diffusion: `0 8px 24px rgba(23, 61, 53, 0.06), 0 2px 6px rgba(23, 61, 53, 0.03)`.
  - **Level 3 (Modal Sheets, Image Viewers)**: Supported by a warm muted backdrop blur (`backdrop-filter: blur(8px); background-color: rgba(23, 61, 53, 0.2)`).

## Shapes

The design system incorporates organic curvature with structural discipline:

- **Cards & Diagnostic Containers**: Standardize on `1rem` to `1.5rem` (`rounded-lg` to `rounded-xl`), presenting gentle, approachable contours that reduce user anxiety.
- **Interactive Form Inputs**: Utilize `0.75rem` (`rounded-md` to `rounded-lg`) for a stable, tactile target.
- **Pills, Audio Controls, & Badges**: Fully rounded `9999px` capsule silhouettes (`rounded-full`) for tags, state indicators, audio player pills, and voice input buttons.

## Components

### Buttons
- **Primary**: Solid `#173D35` fill, `#FFFFFF` text, `0.75rem` border-radius or pill shape. Transitions to `#102B25` on hover. Minimal upward 1px translation.
- **Secondary / Ghost**: Pure `#FFFFFF` background, 1px `#E3E8E4` border, `#252B29` text. Hover brings a subtle background wash of `#F1F5F2` and border shift to `#A9BCAF`.
- **Icon Actions**: Clean circular containers (`w-10 h-10`), soft sage hover accents.

### Badges & Pill Chips
- Built with a full pill radius, compact height (`28px`), and `#EBF1ED` background. Text is `#173D35` at `label-sm` with optional status pips (e.g., green dot for verified scans, amber for benign alerts).

### Input Fields & Controls
- **Text Inputs**: Crisp `#FFFFFF` surface, 1px border (`#E3E8E4`), `0.75rem` border-radius. Focus states trigger a 1px border color change to `#173D35` and a soft ambient ring (`0 0 0 3px rgba(169, 188, 175, 0.25)`).
- **Checkboxes & Radios**: Custom circular and rounded-square nodes in `#E3E8E4`, filling with `#173D35` when active, containing sharp white vector glyphs.

### Segmented Tab Switches
- Enclosed capsule switch with a `#F1F5F2` track. Active tab lifts with a pure `#FFFFFF` background, 1px `#E3E8E4` border, and subtle shadow (`shadow-sm`), transitioning smoothly with spring easing.

### Audio & Microphone Controls (AI Voice Dictation)
- **Microphone Pill**: Circular or capsule action button in `#173D35`. When active/recording, displays an organic pulsing outline tinted in `#A9BCAF`.
- **Waveform Visualizer**: Composed of vertical micro-bars using dynamic heights (2px to 24px) rendered in `#173D35` and `#A9BCAF`, animating rhythmically to simulate real-time voice input capture.
- **Audio Scrub Player**: Compact horizontal bar, `#EBF1ED` track, `#173D35` elapsed fill, and a minimal `#FFFFFF` scrubber handle with a soft border.

### Clinical & Diagnostic Cards
- Minimalist containers housing lesion photography, AI confidence intervals, and condition descriptions. Always framed by a 1px hairline border in `#E3E8E4` with white surface fills, padded with `1.5rem` to `2rem` of internal space.