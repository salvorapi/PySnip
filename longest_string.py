import contextlib
import io

def main():
  zen = io.StringIO()
  with contextlib.redirect_stdout(zen):
    import this
  words = zen.getvalue().replace("\n", " ").split(" ")
  # the output should be..."implementation" :)
  print(max(words, key=len))

if __name__ == '__main__':
  main()