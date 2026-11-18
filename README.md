# Word Counter

An offline, client-side only Android app written in Python (Kivy).
No backend, no internet — everything runs locally on the device.

## What it does
- Shows **Word Counter** at the top.
- Shows a large counter that increases automatically over time, starting from
  a big number (`1,000,000`) and counting toward `102,930,233`.
- Remembers the counter value locally, so it keeps its value after the app is
  closed and reopened (built-in memory).
- Uses the included `LMAO.png` as a full-screen wallpaper behind the UI.
- White, outlined typography for readability against the purple wallpaper.

## Files
- `main.py` — the whole app.
- `LMAO.png` — the full-screen wallpaper (already in the project).
- `buildozer.spec` — Android APK build configuration.
- `.github/workflows/build-apk.yml` — free cloud build (no powerful PC needed).
- `requirements.txt` — Python dependencies.

## Build the APK in the cloud (recommended — no strong PC needed)

Your PC only uploads the source. GitHub's servers do all the compiling for free.

1. Create a free account at https://github.com
2. Create a **new repository** (make it **Public** for free unlimited build minutes).
3. Upload all the files from this folder into the repo — including the
   `.github` folder. If the hidden `.github` folder doesn't upload, create a
   file named `.github/workflows/build-apk.yml` in the web editor and paste in
   the contents of that file.
4. Once the files are uploaded, go to the **Actions** tab at the top of the repo.
   - The build may start automatically. If it doesn't, click **Build Word Counter
     APK** on the left, then **Run workflow** → **Run workflow**.
5. Wait ~10–20 minutes while GitHub builds it.
6. When the run finishes (green checkmark), scroll to the bottom of the run page
   and download the **word-counter-apk** artifact (a ZIP). Unzip it to get the
   `.apk` file.
7. Transfer the `.apk` to your phone and install it (you may need to enable
   **Install unknown apps** in Android settings).

If a build fails, open the red run in the Actions tab and read the log — send me
the last ~30 lines and I'll fix it.

## Build locally (only if you have a Linux machine)
The APK is **not** built here. On Linux/macOS (or Windows via WSL):

```bash
pip install buildozer
buildozer android debug
```

The resulting APK will be in the `bin/` folder.

## Run on desktop (for testing)
```bash
pip install -r requirements.txt
python main.py
```

The counter memory file is stored in Kivy's app-private user data directory,
so it works the same way on desktop and Android.
