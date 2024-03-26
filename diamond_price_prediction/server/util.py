import numpy as np
import json
import pickle
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

__cut_categories = None
__clarity_categories = None
__color_categories = None
__model = None


def get_predicted_price(carat, cut, color, clarity, table, x, y, z, depth=0.0):
    cut_mapping = {"fair": 0, "good": 1, "very good": 2, "premium": 3, "ideal": 4}
    color_mapping = {"j": 0, "i": 1, "h": 2, "g": 3, "f": 4, "e": 5, "d": 6}
    clarity_mapping = {"i1": 0,"si2": 1,"si1": 2,"vs2": 3,"vs1": 4,"vvs2": 5,"vvs1": 6,"if": 7}
    if(y==0.0 or x==0.0 or z==0.0 or table==0.0): return 0.0
    if depth == 0:
        depth = 2 * z / x + y
    x_test = np.zeros(11)
    x_test[0] = carat
    x_test[1] = cut_mapping[cut]
    x_test[2] = color_mapping[color]
    x_test[3] = clarity_mapping[clarity]
    x_test[4] = depth
    x_test[5] = table
    x_test[6] = x
    x_test[7] = y
    x_test[8] = z
    x_test[9] = table / (x + y)
    x_test[10] = x * y * z
    return round(float(__model.predict([x_test])[0]),2)


def get_cut_names():
    return __cut_categories


def get_clarity_categories():
    return __clarity_categories


def get_color_categories():
    return __color_categories


def load_artifacts():
    print("Loading saved artifacts...")
    global __model
    global __cut_categories
    global __clarity_categories
    global __color_categories

    with open("./artifacts/columns.json", "r") as f:
        data = json.load(f)
        __cut_categories = data["cut_categories"]
        __clarity_categories = data["clarity_categories"]
        __color_categories = data["color_categories"]
    with open("./artifacts/xgb_model.pkl", "rb") as f:
        __model = pickle.load(f)

    print("Loading artifacts ... done")


# if __name__ == '__main__':
# load_artifacts()
# print(get_predicted_price(carat=3.23, cut='Ideal', color='D', clarity='IF', depth=61.5, table=55.0, x=3.95, y=3.98, z=2.43))
