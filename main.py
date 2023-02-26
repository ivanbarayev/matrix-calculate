import numpy as np
import json
from json.decoder import JSONDecodeError


# Simple matrix multiplication given 2 matrices
def calculate_matrices(arr_matrix1, arr_matrix2):
    result = np.dot(np.asarray(arr_matrix1), np.asarray(arr_matrix2))
    return np.array(result)


def json_response_logger(error, messages, result):
    with open("response.json", "w") as f:
        json.dump({"error": error, "messages": messages, "result": result}, f)
    return


def main():
    chk_err_matrix = []

    # Load & parse the request
    try:
        with open("request.json", "r") as f:
            index = json.load(f)
            arr_matrix1 = index.get("A")
            arr_matrix2 = index.get("B")

    except JSONDecodeError as e:
        json_response_logger(True, str(e), None)

    if not arr_matrix1:
        chk_err_matrix.append("First Matrix array is not valid !")

    if not arr_matrix2:
        chk_err_matrix.append("Second Matrix array is not valid !")

    if arr_matrix1 and arr_matrix2:
        # Get the result of calculated matrices
        response = calculate_matrices(arr_matrix1, arr_matrix2)
        # write response to file
        json_response_logger(False, None, response.tolist())
    else:
        json_response_logger(True, chk_err_matrix, None)


if __name__ == "__main__":
    main()
