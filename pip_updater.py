import subprocess

print("Basic Python Package Updater with Pip")
get_outdated_packages = "pip list -o"  # Örnek bir terminal komutu
outdated_packages = subprocess.Popen(get_outdated_packages, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

std_output, std_error = outdated_packages.communicate()
outdated_pip_packages = std_output.decode('utf-8')

# Fetch outdated package names
package_lines = outdated_pip_packages.strip().split('\n')[3:]
package_names = [line.split()[0] for line in package_lines]

if len(package_names) == 0:
    print("All packages up-to-date.")

else:
    print("Outdated Python packages:")
    print(outdated_pip_packages)

    for package_name in package_names:
        print("Updating: ", package_name)
        print(subprocess.run("pip install "+package_name+" --upgrade", shell=True, capture_output=True, text=True).stdout)
    print("All packages updated")
