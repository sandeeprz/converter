def converter(feet, inches):
    meter = (feet * 0.3048) + (inches * 0.0254)
    return meter


if __name__ == '__main__':
    print(converter(1, 3))
