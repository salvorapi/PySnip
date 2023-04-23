def main():
  str = "unicode smile string ☺"
  str_to_bytes = str.encode("utf-8")
  bytes_to_str = str_to_bytes.decode("utf-8")
  print(str)
  print(str_to_bytes)
  print(bytes_to_str)
  assert str == bytes_to_str

# end def
if __name__ == "__main__":
  main()
# end main