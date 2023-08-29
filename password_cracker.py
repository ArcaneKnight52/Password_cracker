# password_cracker.py
import argparse
import wordlist_generator
import dictionary_attack
import hash_attack
import brute_force_attack
import threading

def main():
    parser = argparse.ArgumentParser(description="Advanced Password Cracker")
    parser.add_argument("--wordlist", action="store_true", help="Generate wordlist")
    parser.add_argument("--dictionary", action="store_true", help="Perform dictionary attack")
    parser.add_argument("--hash", action="store_true", help="Perform hash attack")
    parser.add_argument("--brute-force", action="store_true", help="Perform brute-force attack")
    parser.add_argument("--hash-algorithm", help="Hash algorithm for hash attack (e.g., sha256)")
    args = parser.parse_args()

    #f args.wordlist:
        # Inside the section where wordlist is generated

    if args.wordlist:
        wordlist = wordlist_generator.generate_wordlist()
        with open('wordlist.txt', 'w') as f:
            f.write('\n'.join(wordlist))
        print("Generated wordlist and saved it to 'wordlist.txt'")

        # wordlist = wordlist_generator.generate_wordlist()
        #print("Generated wordlist with", len(wordlist), "entries.")
    else:
        hashed_password = input("Enter the hashed password: ")

        if args.dictionary:
            wordlist = wordlist_generator.generate_wordlist()
            password, algo = dictionary_attack.dictionary_attack(hashed_password, wordlist)
            if password:
                print("Dictionary attack successful.")
                print("Password:", password)
                print("Hash Algorithm:", algo)
            else:
                print("Dictionary attack unsuccessful.")
        elif args.hash:
            input_password = input("Enter a password to hash: ")
            if hash_attack.hash_attack(hashed_password, input_password, args.hash_algorithm):
                print("Hash attack successful.")
            else:
                print("Hash attack unsuccessful.")
        elif args.brute_force:
            charset = brute_force_attack.generate_charset()

            def perform_brute_force():
                print("Initiating brute-force attack...")
                password, elapsed_time, algo = brute_force_attack.brute_force_attack(hashed_password, charset, 6)
                if password:
                    print("Brute-force attack successful.")
                    print("Password:", password)
                    print("Elapsed Time:", elapsed_time, "seconds")
                    print("Hash Algorithm:", algo)
                else:
                    print("Brute-force attack unsuccessful.")

            brute_force_thread = threading.Thread(target=perform_brute_force)
            brute_force_thread.start()
            brute_force_thread.join()
        else:
            print("No attack selected. Use --wordlist, --dictionary, --hash, or --brute-force flags.")

if __name__ == "__main__":
    main()
