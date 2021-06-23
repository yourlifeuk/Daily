Import Powershell

Get-WindowsFeature *AD-Domain-Services*
Get-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools
Get-Help ADDSForest