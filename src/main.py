from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from schema.users import UserResponseSchema, UserSchema

app = FastAPI()

# ユーザ新規登録
@app.post("/users", response_model=UserResponseSchema)
async def create_user() -> UserResponseSchema:
    # TODO: Implement user creation logic
    return UserResponseSchema(message="ユーザの作成に成功しました。")

# 特定のユーザ情報の取得
@app.get("/users/{user_id}", response_model=UserResponseSchema)
async def get_user_details(user_id: int) -> UserResponseSchema:
    # TODO: Implement user retrieval logic
    print(user_id)
    return UserResponseSchema(message="ユーザ情報の取得に成功しました。")

# ユーザ情報更新
@app.patch("/users/{user_id}", response_model=UserResponseSchema)
async def update_user(user_id: int, user: UserSchema) -> UserResponseSchema:
    # TODO: Implement user update logic
    print(user_id, user)
    return UserResponseSchema(message="ユーザ情報の更新に成功しました。")

# バリデーションエラーのカスタムハンドラ
@app.exception_handler(ValidationError)
async def validation_exception_handler(exc: ValidationError) -> JSONResponse:
    # ValidationErrorが発生した場合にクライアントに返すレスポンス定義
    return JSONResponse(
        # ステータスコード422
        status_code=422,
        # エラーの詳細
        content={
            # Pydanticが提供するエラーのリスト
            "detail": exc.errors(),
        },
    )
