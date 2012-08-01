from configit import ConfigDict

config_dict = ConfigDict(
    name='recursive with configdict',
)

some_other_dict = dict(
    foo='bar',
    answer=42
)

recursive_test = dict(
    first=ConfigDict(
        second=dict(
            last=7.28
        )
    )
)

onions = {
    'lots': dict(
    oflayers='bam!'
    )
}
