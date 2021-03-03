# Rating: ~ 2.1 / 10
# Link: https://open.kattis.com/problems/warehouse

def main():
  cases = int(input())
  for case in range(cases):
    shipments = int(input())
    inventory = dict()
    for shipment in range(shipments):
      delivery = input().split()
      toy = delivery[0]
      count = int(delivery[1])

      if toy not in inventory:
        inventory[toy] = 0
      inventory[toy] += count

    order = sorted(inventory, key=lambda x: (-inventory[x], x))
    print(len(inventory))
    for item in order:
      print(f'{item} {inventory[item]}')


if __name__ == "__main__":
  main()
