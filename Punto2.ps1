[string] $vName = Read-Host -Prompt "Inserte su nombre"

if($vName -eq "")
{
    Write-Error "Invalid input" 
}
else 
{  
    echo "Hola $vName" 
}
