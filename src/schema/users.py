from pydantic import BaseModel, Field


# ユーザ情報を表すスキーマ
class UserSchema(BaseModel):
    user_id: int = Field(
        ...,
        description="ユーザを一意に識別するID番号。データベースで自動的に割り当てられます。",
        examples=[1, 2, 3],
    )

    user_name: str = Field(
        default="",
        description="ユーザ名。任意で設定可能です。",
        examples=["山田太郎", "鈴木一郎", "佐藤花子"],
    )

    mail_address: str = Field(
        default="",
        description="ユーザのメールアドレス。任意で設定可能です。",
        examples=["yamada@example.com", "suzuki@example.com", "sato@example.com"],
    )

    password: str = Field(
        default="",
        description="ユーザのパスワード。任意で設定可能です。",
        examples=["securepassword123"],
    )

# レスポンスで使用する結果用スキーマ
class UserResponseSchema(BaseModel):
    # 処理結果のメッセージ。このフィールドは必須です。
    message: str = Field(
        ...,
        description="ユーザデータ操作の結果を説明するメッセージ。",
        examples=["ユーザの作成に成功しました。", "ユーザ情報の更新に成功しました。"],
    )
