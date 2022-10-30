import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter, status
from typing import List

# router
router = APIRouter(
    tags=["Numbers"],
)


@router.post(
    "/pair-of-numbers",
    status_code=status.HTTP_200_OK,
    summary="get all users records from database",
)
def get_pair_numbers_controller(
    sum_: int,
    list_: List[int],
):
    """
    Get a list of numbers and a sum, return all pairs of numbers that sum up to the sum

    Args:
        sum_: the sum of the pair of numbers
        list_: the list of numbers to search in

    Returns:
        A list of pairs of numbers
    """
    len_list = len(list_)
    response_list = prepare_list(list_, len_list, sum_)
    return response_list


# service
def prepare_list(list_parameter, len_list, int_parameter):
    unordered_map = {}
    response_list = []
    for i in range(len_list):
        # The key to this function is in the difference between
        # the entered number (sum_) and the value of the element
        # that is at index n. Since, if the sum of these two numbers
        # returns to the value of sum_, it can be assumed that
        # they are a suitable pair of numbers
        value_diff = int_parameter - list_parameter[i]
        element_in_list = list_parameter[i]
        # i used a hash table to store the values ​​of the list
        # if the value_diff is in the map, it means that it is
        # a suitable pair with the current element
        if value_diff in unordered_map:
            response_list.append([element_in_list, value_diff])
        # Note: to avoid key duplicates, I counted the frequency of each element in the list
        ## check the frequency of the element in the unordered_map
        if element_in_list in unordered_map:
            unordered_map[element_in_list] += 1
        ## add the element in the unordered_map if it is not present
        else:
            unordered_map[element_in_list] = 1
    # if the response list is empty, return None
    if len(response_list) == 0:
        return None
    # else, return the response list with the first pairs of numbers found
    return response_list[0]

# Create the app
app = FastAPI(
    title="Pair Of Numbers API",
    description="API for pair a list of numbers",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(router)

# Run the app
if __name__ == "__main__":
    uvicorn.run("app:app",host="0.0.0.0",port=8000, reload=True)