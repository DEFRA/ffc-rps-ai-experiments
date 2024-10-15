from utils import get_code, get_filename
from actionCodes import ActionCodes, all_sfi2024_codes, historic_codes


if __name__ == "__main__":
    codes = ActionCodes()
    codes.add_category('SFI2024', all_sfi2024_codes)
    codes.add_category('historic', historic_codes)
