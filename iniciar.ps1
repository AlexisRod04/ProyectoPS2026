
$ErrorActionPreference = "Stop"

Set-Location $PSScriptRoot


Get-Content ".env" | ForEach-Object {
    $linea = $_.Trim()

    if ($linea -and -not $linea.StartsWith("#") -and $linea.Contains("=")) {
        $partes = $linea -split "=", 2
        $nombre = $partes[0].Trim()
        $valor = $partes[1].Trim()

        [Environment]::SetEnvironmentVariable(
            $nombre,
            $valor,
            "Process"
        )
    }
}

py manage.py runserver
