from fastapi import FastAPI
app = FastAPI(title="Winged phrase")

@app.get("/")
async def root():
    return {"mes)s)age": "Hello World"}

from db import get_random_item, add_item, delete_item
@app.get(
    "/get",
    response_description="winged phrase",
    description="Get random phrase from database"
)
def get():
# eOiHTa
    try:
        phrase = get_random_item()
    except IndexError:
        raise HTTPException(404, "Phrase list is empty") # todo check,
    # possibly not correct
    return phrase

@app.post(
    "/add",
    response_description="Added phrase with *id* parameter"
)
# POST 40 /add eHAnoiHTa
def add (phrase: dict):
    phrase_out = add_item(phrase) #
    return phrase_out

@app.delete("/delete", response_description="Result of deletion") # 40
# DELETE /delete
def delete(id: int):
    try:
        delete_item(id)
        return {"message": "OK"}
    except ValueError as e:
        raise HTTPException(404, str(e))
#
# if __name__ == "__main__":
#     app.run(debug=False, host='127.0.0.1', port=8080)