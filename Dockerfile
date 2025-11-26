# Use the official ROS 2 Humble image as our starting point.
# It's like getting a pre-built Ubuntu computer with ROS already installed.
FROM osrf/ros:humble-desktop-full

# Set an environment variable to avoid annoying prompts during installation.
ENV DEBIAN_FRONTEND=noninteractive

# Now, we update the package list and install extra software we want inside our container.
# RUN is used to execute a command inside the container while it's being built.
RUN apt-get update && apt-get install -y \
    python3-pip \          # The Python package installer
    python3-colcon-common-extensions \ # The ROS 2 build tool (colcon)
    git \                  # Version control system (for GitHub)
    wget \                 # A tool to download files from the internet
    nano \                 # A simple text editor for the terminal
    && rm -rf /var/lib/apt/lists/*  # This cleans up to make the image smaller

# (Optional but Recommended) Create a non-root user to avoid file permission issues
# Replace '1000' with your user ID on Ubuntu (find it by running 'id -u' in your Ubuntu terminal)
ARG USER_ID=1000
ARG GROUP_ID=1000
RUN groupadd --gid $GROUP_ID rosuser && \
    useradd --uid $USER_ID --gid $GROUP_ID --create-home rosuser

# Switch to the non-root user
USER rosuser

# Set the default working directory inside the container.
# When we open a terminal, this is where we'll start.
WORKDIR /workspaces/ros2_ws