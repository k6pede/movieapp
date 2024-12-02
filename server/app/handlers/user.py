from fastapi import JSONResponse


@router.get('/me', tags=['user'], summary='ユーザー取得', description='ユーザー情報の取得')
    def get_me(
        
    )->JSONResponse :
        user = 