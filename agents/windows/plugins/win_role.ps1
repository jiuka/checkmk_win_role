$roles = Get-WindowsFeature | Where-Object -Property FeatureType -EQ -Value Role | Where-Object -EQ -Property Installed -Value $true

Write-Host "<<<win_role:sep(59):encoding(cp437)>>>"
foreach ($role in $roles) {
   Write-Host -Separator ";" $role.Name, $role.DisplayName
}