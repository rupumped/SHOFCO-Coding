# Data plan information
data_plan_mb = int(input("Data Plan (MB): "))  # Total data in megabytes
remaining_days = int(input("Days Left: "))   # Days left in billing cycle

# Data usage by activity (in MB)
webpage_mb = 3       # Average webpage
photo_upload_mb = 5  # Uploading a photo
video_minute_mb = 15 # Streaming video (per minute)
audio_minute_mb = 2  # Streaming audio (per minute)

# Calculate daily data limit
daily_data_limit = data_plan_mb / remaining_days

# Calculate how many activities you can do with your daily limit
daily_webpages = daily_data_limit // webpage_mb
daily_photos = daily_data_limit // photo_upload_mb
daily_video_minutes = daily_data_limit // video_minute_mb
daily_audio_minutes = daily_data_limit // audio_minute_mb

# Calculate how many activities you can do with total data
total_webpages = data_plan_mb // webpage_mb
total_photos = data_plan_mb // photo_upload_mb
total_video_minutes = data_plan_mb // video_minute_mb
total_audio_minutes = data_plan_mb // audio_minute_mb

# Display results
print("===== Mobile Data Calculator =====")
print(f"Data Plan: {data_plan_mb} MB for {remaining_days} days")
print(f"Daily Limit: {daily_data_limit:.2f} MB per day")
print("\nDaily Activity Limits:")
print(f"Web Pages: {daily_webpages:.0f} pages")
print(f"Photo Uploads: {daily_photos:.0f} photos")
print(f"Video Streaming: {daily_video_minutes:.0f} minutes")
print(f"Audio Streaming: {daily_audio_minutes:.0f} minutes")
print("\nTotal Plan Activity Limits:")
print(f"Web Pages: {total_webpages:.0f} pages")
print(f"Photo Uploads: {total_photos:.0f} photos")
print(f"Video Streaming: {total_video_minutes:.0f} minutes")
print(f"Audio Streaming: {total_audio_minutes:.0f} minutes")
print("=================================")