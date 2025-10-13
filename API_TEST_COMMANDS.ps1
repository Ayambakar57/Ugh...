# API Test Commands - PowerShell Version
# Run this in PowerShell: .\API_TEST_COMMANDS.ps1

$BaseUrl = "http://127.0.0.1:8000"

Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "1. REGISTER NEW USER" -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan

$registerBody = @{
    code_id = "USR-001"
    full_name = "John Doe"
    username = "johndoe"
    password = "SecurePassword123!"
} | ConvertTo-Json

Invoke-RestMethod -Uri "$BaseUrl/api/auth/register" `
    -Method Post `
    -ContentType "application/json" `
    -Body $registerBody | ConvertTo-Json

Write-Host "`n=========================================" -ForegroundColor Cyan
Write-Host "2. LOGIN (Get Tokens)" -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan

$loginBody = @{
    username = "johndoe"
    password = "SecurePassword123!"
} | ConvertTo-Json

$tokens = Invoke-RestMethod -Uri "$BaseUrl/api/auth/login-json" `
    -Method Post `
    -ContentType "application/json" `
    -Body $loginBody

$tokens | ConvertTo-Json

# Save tokens for later use
$accessToken = $tokens.access_token
$refreshToken = $tokens.refresh_token

Write-Host "`n=========================================" -ForegroundColor Cyan
Write-Host "3. ACCESS PROTECTED ENDPOINT (Get Current User)" -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan

$headers = @{
    "Authorization" = "Bearer $accessToken"
}

Invoke-RestMethod -Uri "$BaseUrl/api/auth/me" `
    -Method Get `
    -Headers $headers | ConvertTo-Json

Write-Host "`n=========================================" -ForegroundColor Cyan
Write-Host "4. REFRESH ACCESS TOKEN" -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan

$refreshBody = @{
    refresh_token = $refreshToken
} | ConvertTo-Json

$newTokens = Invoke-RestMethod -Uri "$BaseUrl/api/auth/refresh" `
    -Method Post `
    -ContentType "application/json" `
    -Body $refreshBody

$newTokens | ConvertTo-Json

Write-Host "`n=========================================" -ForegroundColor Cyan
Write-Host "5. TEST OTHER PROTECTED ENDPOINTS" -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan

Write-Host "`nGetting all users..." -ForegroundColor Yellow
try {
    Invoke-RestMethod -Uri "$BaseUrl/api/users/" `
        -Method Get `
        -Headers $headers | ConvertTo-Json
} catch {
    Write-Host "Error: $_" -ForegroundColor Red
}

Write-Host "`nGetting all companies..." -ForegroundColor Yellow
try {
    Invoke-RestMethod -Uri "$BaseUrl/api/companies/" `
        -Method Get `
        -Headers $headers | ConvertTo-Json
} catch {
    Write-Host "Error: $_" -ForegroundColor Red
}

Write-Host "`n=========================================" -ForegroundColor Cyan
Write-Host "6. CHANGE PASSWORD" -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan

$passwordBody = @{
    old_password = "SecurePassword123!"
    new_password = "NewSecurePassword456!"
} | ConvertTo-Json

try {
    Invoke-RestMethod -Uri "$BaseUrl/api/auth/change-password" `
        -Method Post `
        -Headers $headers `
        -ContentType "application/json" `
        -Body $passwordBody | ConvertTo-Json
} catch {
    Write-Host "Error: $_" -ForegroundColor Red
}

Write-Host "`n=========================================" -ForegroundColor Green
Write-Host "All tests completed!" -ForegroundColor Green
Write-Host "=========================================" -ForegroundColor Green
Write-Host "`nTokens for manual testing:" -ForegroundColor Yellow
Write-Host "Access Token: $accessToken" -ForegroundColor Gray
Write-Host "`nRefresh Token: $refreshToken" -ForegroundColor Gray
