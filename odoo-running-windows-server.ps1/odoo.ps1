# Define the paths to your Odoo environment
$OdooPython = "C:\Program Files\Odoo 19.0.20260225\python\python.exe"
$OdooBin = "C:\Program Files\Odoo 19.0.20260225\server\odoo-bin"

# --- Set your default arguments here ---
# Example: Running with a specific config file or database
$DefaultArgs = @("server")
$localURL = "http://localhost:8069"
if ($args.Count -gt 0) {
    Write-Host "Arguments detected. Running Odoo with: $args" -ForegroundColor Green
	& start $localURL
    & $OdooPython $OdooBin @args
} else {
    Write-Host "No arguments provided. Running with defaults: $DefaultArgs" -ForegroundColor Cyan
	& start $localURL
    & $OdooPython $OdooBin @DefaultArgs
}
