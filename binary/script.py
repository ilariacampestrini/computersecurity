import matplotlib.pyplot as plt

def hex_to_decimal(hex_value):
    # Convert hexadecimal string to decimal
    return int(hex_value.strip('h'), 16)

def read_coordinates(file_path):
    x_coords = []
    y_coords = []
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
        for i, line in enumerate(lines):
            value = float(hex_to_decimal(line.strip()))
            if i % 2 == 0:
                x_coords.append(value)
            else:
                y_coords.append(value)
    
    return x_coords, y_coords

def plot_coordinates(x_coords, y_coords):
    plt.scatter(x_coords, y_coords)
    plt.xlabel('X Coordinates')
    plt.ylabel('Y Coordinates')
    plt.title('Plot of Coordinates')
    plt.grid(True)
    plt.show()

def main():
    file_path = 'maze3.txt'  # Change this to your file path
    x_coords, y_coords = read_coordinates(file_path)
    plot_coordinates(x_coords, y_coords)

if __name__ == "__main__":
    main()
