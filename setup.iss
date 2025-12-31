[Setup]
AppName=Estedad_yabi
AppVersion=1.0
DefaultDirName={pf}\Estedad_yabi
DefaultGroupName=Estedad_yabi
OutputBaseFilename=setup
Compression=lzma
SolidCompression=yes

[Files]
Source: "build\exe.win-amd64-3.11.x\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "build\exe.win-amd64-3.11.x\DLLs\*"; DestDir: "{app}\DLLs"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Estedad_yabi"; Filename: "{app}\Estedad_yabi.exe"
Name: "{group}\Uninstall Your App Name"; Filename: "{uninstallexe}"

[Run]
Filename: "{app}\Estedad_yabi.exe"; WorkingDir: "{app}"; Flags: nowait postinstall skipifsilent
