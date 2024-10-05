# PowerShell script to execute two Python scripts sequentially
# Define the paths to the Python scripts
$pythonScript1 = "C:\Users\rastr\Documents\GitHub\Python_Programs\Scripts\Automate\Utility\removeBg.py"
$pythonScript2 = "C:\Users\rastr\Documents\GitHub\Python_Programs\Scripts\Automate\Utility\centerCrop.py"

# Execute the first Python script
Write-Host "Running Script 1: $pythonScript1"
$script1Result = python $pythonScript1

# Check if the first script ran successfully
if ($LASTEXITCODE -eq 0) {
    Write-Host "Script 1 executed successfully."

    # Execute the second Python script only if the first one was successful
    Write-Host "Running Script 2: $pythonScript2"
    python $pythonScript2
} else {
    Write-Host "Script 1 failed. Script 2 will not be executed."
}

# After both scripts (if applicable) have been executed, prompt the user to press any key to continue
Write-Host "`nProcess complete. Press any key to close this window."
$x = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")