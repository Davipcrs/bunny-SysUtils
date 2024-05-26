import sys
import win32api
import win32com.shell.shell as shell  # type: ignore
import win32security

# Define the shell constant
SHELL_EXECUTE = 'runas'


def isAdmin():
    """Check if the script is running with administrative privileges."""
    try:
        # Get the current process token
        token_handle = win32security.OpenProcessToken(
            win32api.GetCurrentProcess(), win32security.TOKEN_QUERY)
        # Get the elevation information
        elevation = win32security.GetTokenInformation(
            token_handle, win32security.TokenElevation)
        return elevation
    except Exception as e:
        print(f"Failed to check admin status: {e}")
        return False


def elevate():
    """Relaunch the script with administrative privileges."""
    # Get the current executable path
    executable = sys.executable
    params = ' '.join([f'"{param}"' for param in sys.argv])

    # Relaunch the script with elevated privileges
    shell.ShellExecuteEx(lpVerb=SHELL_EXECUTE,
                         lpFile=executable, lpParameters=params)
    sys.exit(0)
