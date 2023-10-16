from moviepy.editor import VideoFileClip
from PIL import Image

def resize_video_for_instagram(input_video_path, insta_width, insta_height):
  """Resizes a video to fit Instagram dimensions.

  Args:
    input_video_path: The path to the input video file.
    insta_width: The width of the Instagram canvas.
    insta_height: The height of the Instagram canvas.

  Returns:
    A VideoFileClip object representing the resized video.
  """

  # Load the input video.
  input_video = VideoFileClip(input_video_path)

  # Resize the video frame by frame using Pillow.
  resized_frames = []
  for frame in input_video.iter_frames():
    resized_frame = Image.fromarray(frame).resize((insta_width, insta_height))
    resized_frames.append(resized_frame)

  # Create a new VideoFileClip object from the resized frames.
  resized_video = VideoFileClip(resized_frames)

  # Return the resized video.
  return resized_video


# Example usage:
input_video_path = "pythonfiles/git.mp4"
insta_width = 1080
insta_height = 1920

output_video = resize_video_for_instagram(input_video_path, insta_width, insta_height)
output_video.write_videofile("output_instagram_video.mp4", codec="libx264")
output_video.close()
