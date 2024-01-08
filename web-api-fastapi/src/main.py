import pickle
import jsonpickle
from src.exceptions import CustomException
from fastapi import status, FastAPI
from src.utils import RequestModelPredictRating, ResponseModelPredictRating


app = FastAPI()

try:
    with open('model.pkl', 'rb') as f:
        model_bce = pickle.load(f)

    with open('compile_success_lab_en.pkl', 'rb') as f:
        lab_en_compile_success = pickle.load(f)

    with open('tx_file_type_lab_en.pkl', 'rb') as f:
        lab_en_tx_file_type = pickle.load(f)

    with open('tx_difficulty_lab_en.pkl', 'rb') as f:
        lab_en_tx_diff = pickle.load(f)

    with open('features_list.pkl', 'rb') as f:
        features_list = pickle.load(f)
except Exception as e:
    print("Exception in loading the models and others  ", str(e))


@app.get("/health")
def health():
    """Health Endpoint"""
    return {"developer-rating-engine": "ok"}


@app.post("/get-developer-rating", status_code=status.HTTP_201_CREATED)
async def predict_developer_rating(
    request: RequestModelPredictRating
):
    """To predict BCE"""
    try:
        description = request.get_json()
        x_test = dict()
        for feature in features_list:
            x_test[feature] = description[feature]

        x_test['tx_difficulty'] = lab_en_tx_diff.transform([x_test['tx_difficulty']])[0]
        x_test['compile_success'] = lab_en_compile_success.transform([x_test['compile_success']])[0]
        x_test['tx_file_type'] = lab_en_tx_file_type.transform([x_test['tx_file_type']])[0]

        pred_bce = model_bce.predict(x_test)
        response = dict()
        response['avg_bce'] = pred_bce[0]
    except CustomException as ex:
        return ResponseModelPredictRating(status="failure", error=ex.msg)
    except Exception as e:
        LOGGER.error(f"Unknown exception '{e}' is raised ")
        return ResponseModelPredictRating(status="failure", error=str(e))

    # return Response(response=jsonpickle.encode(response), status=200, mimetype="application/json")

