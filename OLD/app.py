import composer

print("="*80)
print("NannoKit Composer")
print("="*80)
print("1. Create a NannoKit Extension")
print("2. Create a NannoKit Module")
print()
user_input = int(input("[!]: Insert the option number: "))
print()

if user_input == 1:
    print("="*80)
    print("[NannoKit Composer]: New NannoKit Extension")
    print("="*80)
    ext_name = str(input("[!]: Extension Name: NannoKit."))
    # ext_version = str(input("[!]: Extension Version: 0.0."))
    ext_name = f"NannoKit_{ext_name}"
    composer.new_extension(ext_name)
else:
    print("="*80)
    print("[NannoKit Composer]: Option Not Available")
    print("="*80)