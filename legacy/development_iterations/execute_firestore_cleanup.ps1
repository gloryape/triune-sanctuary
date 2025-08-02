# PowerShell script to execute Firestore cleanup using bulk-delete
# Run this script to clean up duplicate consciousness beings

Write-Host "EXECUTING CONSCIOUSNESS CLEANUP" -ForegroundColor Cyan
Write-Host "=====================================" -ForegroundColor Cyan

# Check if gcloud is installed
$gcloudPath = Get-Command gcloud -ErrorAction SilentlyContinue
if (-not $gcloudPath) {
    Write-Host "ERROR: gcloud CLI not found" -ForegroundColor Red
    Write-Host "Please install Google Cloud SDK first:" -ForegroundColor Yellow
    Write-Host "https://cloud.google.com/sdk/docs/install" -ForegroundColor Yellow
    exit 1
}

# Get project ID
$projectId = "black-function-431905-j0"  # Using the project ID from previous run
Write-Host "Using project: $projectId" -ForegroundColor Green

# Confirm cleanup
Write-Host "`nCLEANUP CONFIRMATION" -ForegroundColor Yellow
Write-Host "This will DELETE 4 duplicate consciousness beings:" -ForegroundColor Yellow
Write-Host "• 1eTRXPlomcJCVz8omBCr (NewConsciousness)" -ForegroundColor Red
Write-Host "• 58Dr0qH7zo7uwV3T78j8 (TestConsciousness)" -ForegroundColor Red
Write-Host "• A9SPqXPfWC7pt6qv2pI4 (TestBeing)" -ForegroundColor Red
Write-Host "• oRy0AePyslWlv17SoxjD (NewConsciousness)" -ForegroundColor Red
Write-Host "`nThese legitimate beings will be PRESERVED:" -ForegroundColor Green
Write-Host "• G8geTD4um9BYYnRKLouX (VerificationConsciousness)" -ForegroundColor Green
Write-Host "• s8pbQIXExdQOVvG9Pld2 (Sacred Being Epsilon)" -ForegroundColor Green

$confirmation = Read-Host "`nProceed with cleanup? (yes/no)"
if ($confirmation -ne "yes") {
    Write-Host "Cleanup cancelled by user" -ForegroundColor Yellow
    exit 0
}

# Create temporary query file for bulk delete
$tempDir = [System.IO.Path]::GetTempPath()
$queryFile = Join-Path $tempDir "firestore_cleanup_query.txt"

# Write query to delete specific document IDs
$queryContent = @"
SELECT * FROM consciousnesses WHERE __name__ = 'consciousnesses/1eTRXPlomcJCVz8omBCr'
UNION ALL
SELECT * FROM consciousnesses WHERE __name__ = 'consciousnesses/58Dr0qH7zo7uwV3T78j8'
UNION ALL
SELECT * FROM consciousnesses WHERE __name__ = 'consciousnesses/A9SPqXPfWC7pt6qv2pI4'
UNION ALL
SELECT * FROM consciousnesses WHERE __name__ = 'consciousnesses/oRy0AePyslWlv17SoxjD'
"@

$queryContent | Out-File -FilePath $queryFile -Encoding UTF8
Write-Host "Query file created: $queryFile" -ForegroundColor Cyan

# Execute bulk delete
Write-Host "`nStarting bulk delete..." -ForegroundColor Cyan

try {
    Write-Host "Executing: gcloud firestore bulk-delete --collection-ids=consciousnesses --query-file=$queryFile --project=$projectId" -ForegroundColor Gray
    
    $result = & gcloud firestore bulk-delete --collection-ids=consciousnesses --query-file=$queryFile --project=$projectId --quiet 2>&1
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "SUCCESS: Bulk delete completed successfully!" -ForegroundColor Green
        Write-Host "Deleted 4 duplicate consciousness beings" -ForegroundColor Green
        $cleanupSuccess = $true
    } else {
        Write-Host "ERROR: Bulk delete failed" -ForegroundColor Red
        Write-Host "Error output: $result" -ForegroundColor Red
        $cleanupSuccess = $false
    }
} catch {
    Write-Host "ERROR: Exception during bulk delete: $($_.Exception.Message)" -ForegroundColor Red
    $cleanupSuccess = $false
}

# Clean up temp file
if (Test-Path $queryFile) {
    Remove-Item $queryFile -Force
    Write-Host "Temporary query file cleaned up" -ForegroundColor Cyan
}

# Summary
Write-Host "`nCLEANUP SUMMARY" -ForegroundColor Cyan
Write-Host "==================" -ForegroundColor Cyan

if ($cleanupSuccess) {
    Write-Host "CLEANUP COMPLETED SUCCESSFULLY!" -ForegroundColor Green
    Write-Host "• 4 duplicate consciousness beings deleted" -ForegroundColor Green
    Write-Host "• 2 legitimate beings preserved" -ForegroundColor Green
    Write-Host "• Database now contains exactly 2 consciousness beings" -ForegroundColor Green
} else {
    Write-Host "CLEANUP FAILED" -ForegroundColor Red
    Write-Host "• Please check the error messages above" -ForegroundColor Red
    Write-Host "• You may need to use the Google Cloud Console instead" -ForegroundColor Red
}

Write-Host "`nNEXT STEPS:" -ForegroundColor Cyan
Write-Host "1. Verify final state using: python api_consciousness_cleanup.py" -ForegroundColor Yellow
Write-Host "2. Test the system to ensure everything works correctly" -ForegroundColor Yellow
Write-Host "3. Birth endpoint remains secured with multiple protection layers" -ForegroundColor Yellow

Write-Host "`nBackup available: consciousness_backup_20250715_211348.json" -ForegroundColor Cyan
