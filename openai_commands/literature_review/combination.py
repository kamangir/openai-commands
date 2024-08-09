import glob
import pandas as pd
from blueness import module
from abcli import file
from abcli.modules import objects
from openai_commands import NAME
from openai_commands.logger import logger

NAME = module.name(__file__, NAME)


def combine(
    object_name_1: str,
    object_name_2: str,
    object_name: str,
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
        filename_name_and_Extension = file.name_and_extension(filename_1)

        filename_2 = objects.path_of(
            filename_name_and_Extension,
            object_name_2,
        )

        if not file.exist(filename_2):
            logger.warning(
                "missing in object-2 [{}]: {}".format(
                    object_name_2,
                    filename_name_and_Extension,
                )
            )
            continue

        success_1, df_1 = file.load_dataframe(filename_1)
        success_2, df_2 = file.load_dataframe(filename_2)
        if not success_1 or not success_2:
            logger.warning("bad file: {}".format(filename_name_and_Extension))
            continue

        df = pd.merge(df_1, df_2, left_index=True, right_index=True)

        if not file.save_csv(
            objects.path_of(
                filename_name_and_Extension,
                object_name_2,
            ),
            df,
        ):
            return False

    return True
