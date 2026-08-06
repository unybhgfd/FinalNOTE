"""
用学而思的 OSS 下载数据集
"""


from typing import Literal
from keras.src.utils.file_utils import get_file

__all__ = [
    "download_dataset"
]

BASE_URL = "https://livefile.xesimg.com/programme/python_assets/"

def get_args(fname: str, oss_filename: str):
    return {"fname": fname, "origin": BASE_URL + oss_filename}

OSS_FILENAMES: dict[str, dict[str, str] | list[dict[str, str]]] = {
    "boston_housing": get_args("boston_housing.npz", "5f3579cbda725d77bd53d8656fc6aa0f.npz"),
    "california_housing": get_args("california_housing.npz", "6eb4f9c4fc5096097bf618d115c3810b.npz"),
    "cifar10": get_args("cifar-10-batches-py-target", "c58f30108f718f92721af3b95e74349a.gz"),
    "cifar100": get_args("cifar-100-python-target", "eb9058c3a382ffc7106e4002c42a8d85.gz"),
    "fashion_mnist": [
        get_args("train-labels-idx1-ubyte.gz", "25c81989df183df01b3e8a0aad5dffbe.gz"),
        get_args("train-images-idx3-ubyte.gz", "8d4fb7e6c68d591d4c3dfef9ec88bf0d.gz"),
        get_args("t10k-labels-idx1-ubyte.gz", "bb300cfdad3c16e7a12a480ee83cd310.gz"),
        get_args("t10k-images-idx3-ubyte.gz", "bef4ecab320f06d8554ea6380940ec79.gz")
    ],
    "imdb": get_args("imdb.npz", "599dadb1135973df5b59232a0e9a887c.npz"),
    "mnist": get_args("mnist.npz", "8a61469f7ea1b51cbae51d4f78837e45.npz"),
    "reuters": get_args("reuters.npz", "87aedbeb0cb229e378797a632c1997b6.npz")
}

def download_dataset(name: Literal[
    "boston_housing",
    "california_housing",
    "cifar10",
    "cifar100",
    "fashion_mnist",
    "imdb",
    "mnist",
    "reuters",
]):
    """用学而思的 OSS 下载数据集

    示例：

    ```python
    # 使用 Keras 的文件下载接口用 OSS 下载文件到默认位置
    download_dataset("mnist")

    # 加载数据时会检测到下载的文件然后使用
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    ```
    """
    args_list = OSS_FILENAMES.get(name)
    if args_list is None:
        raise FileNotFoundError(f"不支持下载 {name} 数据集")
    if isinstance(args_list, dict):
        args_list = [args_list]
    for args in args_list:
        get_file(
            **args  # type: ignore
        )
