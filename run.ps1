# QR Code Generator launcher — creates/validates venv, installs deps, runs app.

$ErrorActionPreference = 'Stop'

$APP_NAME   = "QRCodeGenerator"
$ENTRY      = "code\qr_code_gui.py"
$VENV_DIR   = "venv"
$REQUIREMENTS = "requirements.txt"

Set-Location $PSScriptRoot

function Test-VenvValid {
    $cfg = Join-Path $VENV_DIR "pyvenv.cfg"
    if (-not (Test-Path $cfg)) { return $false }
    $homeLine = Select-String -Path $cfg -Pattern '^\s*home\s*=' | Select-Object -First 1
    if (-not $homeLine) { return $false }
    $pythonHome = ($homeLine.Line -split '=', 2)[1].Trim()
    return (Test-Path (Join-Path $pythonHome "python.exe"))
}

function Find-Python {
    foreach ($cmd in @("python", "python3")) {
        $found = Get-Command $cmd -ErrorAction SilentlyContinue
        if ($found) { return $found.Source }
    }
    return $null
}

if ((Test-Path $VENV_DIR) -and -not (Test-VenvValid)) {
    Write-Host "[$APP_NAME] Existing venv has a broken Python reference, recreating..."
    Remove-Item -Recurse -Force $VENV_DIR
}

if (-not (Test-Path $VENV_DIR)) {
    Write-Host "[$APP_NAME] Creating virtual environment..."
    $pythonExe = Find-Python
    if (-not $pythonExe) {
        Write-Error "Error: no working Python found. Install Python from https://python.org"
        exit 1
    }
    Write-Host "[$APP_NAME] Using Python: $pythonExe"
    & $pythonExe -m venv $VENV_DIR
    if ($LASTEXITCODE -ne 0) { Write-Error "Error: Failed to create venv."; exit 1 }
}

$activateScript = Join-Path $VENV_DIR "Scripts\Activate.ps1"
if (-not (Test-Path $activateScript)) {
    Write-Error "Error: cannot find venv activate script"
    exit 1
}
& $activateScript

$marker = Join-Path $VENV_DIR ".deps_installed"
$installDeps = $false
if (-not (Test-Path $marker)) {
    $installDeps = $true
} elseif ((Get-Item $REQUIREMENTS).LastWriteTime -gt (Get-Item $marker).LastWriteTime) {
    $installDeps = $true
}

if ($installDeps) {
    Write-Host "[$APP_NAME] Installing dependencies..."
    python -m pip install --upgrade pip -q
    pip install -r $REQUIREMENTS -q
    New-Item -ItemType File -Path $marker -Force | Out-Null
}

python $ENTRY @args
