@ECHO OFF
SETLOCAL ENABLEEXTENSIONS

@REM name of the script (without the file extension)
SET me=%~n0
@REM parent path to the script 
SET parent=%~dp0
@REM full path to the current directory (same as 'parent' without a final backslash)
SET var=%cd%

@REM when the hour is less then 10, returns ' 1' for example, not '01';
@REM the if block below addresses that.
IF %TIME:~0,2% LSS 10 (
    SET hh=^0%TIME:~1,1%
) ELSE (
    SET hh=%TIME:~0,2%) 

@REM set the current timestamp
SET timestamp=%DATE:~0,2%%DATE:~3,2%%DATE:~6,4%.%hh%%TIME:~3,2%%TIME:~6,2%

ECHO. && ECHO %me%: ___switching directory to Outsiders17711.FastPages___
CD /d H:\0ut51d3r5.17711\Google Drive\_hlu.Projects\Outsiders17711.FastPages

ECHO. && ECHO %me%: ___checking status___
git status

ECHO. && ECHO %me%: ___adding changes___
git add .

ECHO. && ECHO %me%: ___committing changes___
git commit -m "%timestamp%: blog repository update..." -m "syncing Outsiders17711.FastPages with Mein.platz"

ECHO. && ECHO %me%: ___setting the remote repository___
git remote set-url origin https://github.com/Outsiders17711/Outsiders17711.FastPages.git
git remote -v

ECHO. && ECHO %me%: **___pushing to remote___**
git push

ECHO. && ECHO %me%: ___pulling to sync history with local___
git pull

ECHO. && ECHO %me%: ___double-checking status___
git status