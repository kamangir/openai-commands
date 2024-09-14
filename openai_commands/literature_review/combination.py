import glob
import pandas as pd

from blueness import module
from blue_objects import file, objects

from openai_commands import NAME
from openai_commands.logger import logger

NAME = module.name(__file__, NAME)


def combine(
    object_name_1: str,
    object_name_2: str,
    object_name: str,
    log: bool = True,
) -> bool:
    logger.info(
        "{}.combine: {} + {} -> {}".format(
            NAME,
            object_name_1,
            object_name_2,
            object_name,
        )
    )

    for filename_1 in glob.glob(objects.path_of("*.csv", object_name_1)):
        filename_name_and_extension = file.name_and_extension(filename_1)

        filename_2 = objects.path_of(
            filename_name_and_extension,
            object_name_2,
        )

        if not file.exists(filename_2):
            logger.warning(
                "missing in object-2 [{}]: {}".format(
                    object_name_2,
                    filename_name_and_extension,
                )
            )
            continue

        success_1, df_1 = file.load_dataframe(filename_1, log=log)
        success_2, df_2 = file.load_dataframe(filename_2, log=log)
        if not success_1 or not success_2:
            logger.warning("bad file: {}".format(filename_name_and_extension))
            continue

        df = pd.concat([df_1, df_2], axis=1)
        df = df.loc[:, ~df.columns.duplicated()]

        if not file.save_csv(
            objects.path_of(
                filename_name_and_extension,
                object_name,
            ),
            df,
            log=log,
        ):
            return False

    return True
