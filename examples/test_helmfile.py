import asyncio
import os
import sys
from pathlib import Path

# Add the parent directory to the Python path
current_dir = Path(__file__).parent
project_root = current_dir.parent.parent
sys.path.append(str(project_root))

# Import the server module directly
from mcp_helmfile.server import execute_helmfile, sync_helmfile

async def cleanup_helmfile(helmfile_path: str):
    """Clean up Helmfile releases."""
    print("\nCleaning up Helmfile releases...")
    result = await execute_helmfile(f"helmfile -f {helmfile_path} destroy")
    print(f"Cleanup result: {result}")
    return result

async def test_helmfile():
    # Get the absolute path to the sample Helmfile
    helmfile_path = os.path.join(current_dir, "sample-helmfile.yaml")
    
    try:
        # Test helmfile list
        print("\nTesting helmfile list...")
        result = await execute_helmfile(f"helmfile -f {helmfile_path} list")
        print(f"List result: {result}")
        
        # Test helmfile sync
        print("\nTesting helmfile sync...")
        result = await sync_helmfile(helmfile_path)
        print(f"Sync result: {result}")
        
        if result["status"] == "error":
            print("Error during sync, cannot proceed with status check")
            return
            
        # Wait a bit for the release to be ready
        print("\nWaiting for release to be ready...")
        await asyncio.sleep(10)
        
        # Test helmfile status
        print("\nTesting helmfile status...")
        result = await execute_helmfile(f"helmfile -f {helmfile_path} status")
        print(f"Status result: {result}")
        
    except Exception as e:
        print(f"Error during testing: {str(e)}")
        raise
    finally:
        # Always attempt cleanup, even if there were errors
        await cleanup_helmfile(helmfile_path)

if __name__ == "__main__":
    asyncio.run(test_helmfile())