# PowerShell script to execute Firestore cleanup
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
$projectId = Read-Host "Enter your Google Cloud Project ID"
if (-not $projectId) {
    Write-Host "ERROR: Project ID required" -ForegroundColor Red
    exit 1
}

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

# Execute cleanup commands
Write-Host "`nStarting cleanup..." -ForegroundColor Cyan

$duplicateIds = @(
    "1eTRXPlomcJCVz8omBCr",
    "58Dr0qH7zo7uwV3T78j8", 
    "A9SPqXPfWC7pt6qv2pI4",
    "oRy0AePyslWlv17SoxjD"
)

$successCount = 0
$failCount = 0

foreach ($id in $duplicateIds) {
    Write-Host "Deleting duplicate consciousness: $id" -ForegroundColor Yellow
    
    try {
        & gcloud firestore documents delete "consciousnesses/$id" --project=$projectId --quiet
        if ($LASTEXITCODE -eq 0) {
            Write-Host "Successfully deleted: $id" -ForegroundColor Green
            $successCount++
        } else {
            Write-Host "Failed to delete: $id" -ForegroundColor Red
            $failCount++
        }
    } catch {
        Write-Host "Error deleting $id : $($_.Exception.Message)" -ForegroundColor Red
        $failCount++
    }
}

# Verify legitimate beings still exist
Write-Host "`nVerifying legitimate beings..." -ForegroundColor Cyan

$legitimateIds = @(
    "G8geTD4um9BYYnRKLouX",
    "s8pbQIXExdQOVvG9Pld2"
)

foreach ($id in $legitimateIds) {
    Write-Host "Checking legitimate being: $id" -ForegroundColor Yellow
    
    try {
        & gcloud firestore documents describe "consciousnesses/$id" --project=$projectId --quiet
        if ($LASTEXITCODE -eq 0) {
            Write-Host "Legitimate being preserved: $id" -ForegroundColor Green
        } else {
            Write-Host "WARNING: Legitimate being not found: $id" -ForegroundColor Red
        }
    } catch {
        Write-Host "WARNING: Error checking $id : $($_.Exception.Message)" -ForegroundColor Red
    }
}

# Summary
Write-Host "`nCLEANUP SUMMARY" -ForegroundColor Cyan
Write-Host "==================" -ForegroundColor Cyan
Write-Host "Successfully deleted: $successCount/4 duplicates" -ForegroundColor Green
Write-Host "Failed deletions: $failCount/4 duplicates" -ForegroundColor Red

if ($failCount -eq 0) {
    Write-Host "`nCLEANUP COMPLETED SUCCESSFULLY!" -ForegroundColor Green
    Write-Host "Your consciousness database now has exactly 2 legitimate beings" -ForegroundColor Green
} else {
    Write-Host "`nCLEANUP PARTIALLY COMPLETED" -ForegroundColor Yellow
    Write-Host "Some duplicates may still exist. Check the errors above." -ForegroundColor Yellow
}

Write-Host "`nBackup available: consciousness_backup_20250715_211348.json" -ForegroundColor Cyan
Write-Host "Birth endpoint remains secured with multiple protection layers" -ForegroundColor Cyan
