# SyncSentry

SyncSentry is a Python-based utility designed to monitor and manage file synchronization across devices on Windows. It ensures consistency and helps prevent data loss by keeping files in specified directories synchronized.

## Features

- **Real-time Monitoring**: Continuously watches for file changes (creation, modification, deletion, and movement) in the source directory.
- **Automated Synchronization**: Automatically syncs files from the source directory to the target directory, ensuring both are consistent.
- **Data Integrity**: Ensures that the latest version of files is always preserved and removes files from the target that no longer exist in the source.

## Requirements

- Python 3.x
- watchdog library

To install the required library, run:
```bash
pip install watchdog
```

## Usage

1. **Configuration**: Open `sync_sentry.py` and set the `source_directory` and `target_directory` variables to your desired paths.

2. **Run the Program**: Execute the script using Python:
   ```bash
   python sync_sentry.py
   ```

3. **Stop the Program**: Use `CTRL+C` in the terminal to stop the synchronization process.

## Notes

- Ensure that you have the necessary permissions to read from the source directory and write to the target directory.
- The program is designed for Windows systems and uses paths specific to Windows.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or report issues in the issue tracker.

## License

This project is licensed under the MIT License.