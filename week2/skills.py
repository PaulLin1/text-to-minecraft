from math import floor

def place_block(bot, block_type, x, y, z, place_on='bottom'):
    """
    Places a block in minecraft
    :param bot: The bot that will place the block
    :param block_type: Name of the block
    :param x: X-coordinate of the block
    :param y: Y-coordinate of the block
    :param z: Z-coordinate of the block
    :param place_on:
    :return: True if block is placed, False otherwise
    """