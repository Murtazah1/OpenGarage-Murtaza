# mp4_to_gif.py
import argparse
import os
import sys

import ffmpeg

# from ..ffm_convertor import FFMConvertor


class FFMConvertor:
    # i just discovered what this staticmethod python decorator is.
    # afaik, you use this whenever you have a member function that is not manipulating and class variable data,
    # thus you declare it as a staatic method so that it cannot access the `self.` variables?
    @staticmethod
    def convert_webm_to_mp4_module(input_webm_path, output_mp4_path):
        """let's convert this .webm file to .mp4, boss!"""
        try:
            input_video = ffmpeg.input(input_webm_path)
            stream = ffmpeg.output(input_video, output_mp4_path)
            ffmpeg.run(stream)
            print(
                f"success! converted '{input_webm_path}' to '{output_mp4_path}', dude!"
            )
        except Exception as e:
            print("watch out bruh! an error occurred:", e)

    @staticmethod
    def convert_mp4_to_gif_module(
        input_mp4_path, output_gif_path, start_time, duration
    ):
        """let's transform this .mp4 file into a stunning .gif, my friend!"""
        try:
            # Create the input stream
            input_stream = ffmpeg.input(input_mp4_path, ss=start_time, t=duration)

            # Create a complex filtergraph
            split = ffmpeg.filter_multi_output(input_stream, "split")
            palette = ffmpeg.filter(split[0], "palettegen")
            output = ffmpeg.filter([split[1], palette], "paletteuse")

            # Run the conversion
            ffmpeg.output(output, output_gif_path).overwrite_output().run()

            print(
                f"success! converted '{input_mp4_path}' to '{output_gif_path}', dude!"
            )
        except Exception as e:
            print("whoa dude! like, an error occurred:", e)


def parse_arguments():
    """time to grab some arguments, let's do this!"""
    parser = argparse.ArgumentParser(
        description="convert a .mp4 file to .gif format, gang!"
    )

    # provide absolute path of input .mp4
    parser.add_argument(
        "-ip",
        "--input-path",
        dest="input_mp4_path",
        required=True,
        help="yo, give me the path to your .mp4 file, broski!",
        metavar="INPUT_MP4_PATH",
    )

    # add file name of output including .gif extension
    parser.add_argument(
        "-of",
        "--output-file",
        dest="output_gif_file",
        help="what's the name you wanna give to the delicious .gif file, my dude?",
        metavar="OUTPUT_GIF",
        default="output.gif",
    )

    return parser.parse_args()


def get_file_paths(args):
    """let's build those file paths like a champ!"""
    current_directory = os.path.dirname(os.path.abspath(__file__))

    if args.input_mp4_path is None:
        print(
            "bro, you can't show up to a party empty handed. give me that full path to your .mp4 file!"
        )
        print("use the -h option to see usage information")
        sys.exit(2)
    else:
        input_mp4_path = args.input_mp4_path

    output_dir = "output/"
    output_gif_path = os.path.join(current_directory, output_dir, args.output_gif_file)

    return input_mp4_path, output_gif_path


def main():
    """main event, baby!"""
    ffm = FFMConvertor()
    args = parse_arguments()

    # compute file path from args, feed as params into function
    input_mp4_path, output_gif_path = get_file_paths(args)
    ffm.convert_mp4_to_gif_module(input_mp4_path, output_gif_path, 0, 5)
    # ffm.convert_mp4_to_gif_module(input_mp4_path, output_gif_path)


if __name__ == "__main__":
    main()
