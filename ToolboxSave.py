import os
import pyperclip

def main():
    determination = True
    file_deciding = True
    while determination:
        while file_deciding:
            try:
                filepath = input(str("Please enter the file path: "))
                file_deciding = False
            except ValueError:
                print("Please enter a valid file path")
            except Exception as e:
                print(f"An error occurred: {e}")
        try:
            filename = input("Please enter the files name:")
            determination = False
        except Exception as e:
            print(f"An error occurred: {e}")
        if not filename.endswith(".txt"):
            filename += ".txt"
    clipboard_data = pyperclip.paste()
    file_save(filepath+"\\"+filename, clipboard_data)

def file_save(filepath, data):
    try:
        outfile = open(filepath, "w", encoding= "utf-8")
        outfile.write(data)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        try:
            outfile.close()
        except Exception as e:
            print(f"An error occurred: {e}")

main()