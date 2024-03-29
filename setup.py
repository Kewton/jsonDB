from setuptools import setup, find_packages

setup(
    name='localjsondb',  # パッケージ名
    version='0.1.3',  # バージョン
    author='kewton',  # 著者名
    author_email='newtons.boiled.clock@gmail.com',  # 著者のメールアドレス
    description='A short description of the package',  # パッケージの短い説明
    #long_description=open('README.md').read(),  # 長い説明（通常はREADME）
    #long_description_content_type='text/markdown',  # 長い説明のコンテントタイプ
    url='https://github.com/Kewton/jsonDB',  # プロジェクトのURL
    packages=find_packages(exclude=('tutorial',"docs", "tests")),  # パッケージのインクルード（テストやドキュメントを除外）
    install_requires=[  # 依存関係のリスト
        'pysondb',
        'pydantic',
    ],
    classifiers=[  # パッケージの分類情報
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',  # サポートするPythonのバージョン
)
