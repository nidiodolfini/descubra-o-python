IS_RELEASE_SERVER = input()
bool(IS_RELEASE_SERVER)
if IS_RELEASE_SERVER == 'true':
    DEBUG = False
else:
    DEBUG = True

print(DEBUG)