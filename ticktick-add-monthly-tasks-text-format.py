#!/usr/bin/env python3
"""
Enhanced Week Scheduler Script
Automates the creation of weekly schedules with proper logging and error handling.
"""

import random
import time
import pyautogui
import datetime
import logging
import json
import argparse
from pathlib import Path
from dataclasses import dataclass
from typing import List, Optional, Tuple
import sys

# Configuration
@dataclass
class Config:
    """Configuration class for the scheduler"""
    single_week_no: int = 1
    press_delay: float = 1.0
    write_delay: float = 1.0
    hotkey_delay: float = 2.0
    scroll_lines: int = 20
    max_scroll_down: int = -999
    press_count_threshold: int = 10
    safety_delay: float = 5.0
    
    # Coordinates (make these configurable)
    click_coordinates: Tuple[int, int] = (1400, 260)
    
    # Time slots
    time_slots: List[str] = None
    
    def __post_init__(self):
        if self.time_slots is None:
            self.time_slots = ["06:00-12:00", "12:00-18:00", "18:00-20:00"]

class WeekScheduler:
    """Main class for handling week scheduling automation"""
    
    def __init__(self, config: Config):
        self.config = config
        self.press_count = 0
        self.logger = self._setup_logging()
        self.stats = {
            'weeks_processed': 0,
            'tasks_created': 0,
            'errors': 0,
            'start_time': None,
            'end_time': None
        }
        
        # PyAutoGUI safety settings
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.1
        
    def _setup_logging(self) -> logging.Logger:
        """Setup logging configuration"""
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        
        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # File handler
        file_handler = logging.FileHandler(
            log_dir / f"week_scheduler_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        )
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        
        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        
        # Logger setup
        logger = logging.getLogger('WeekScheduler')
        logger.setLevel(logging.DEBUG)
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        return logger
    
    def safe_keyboard_write(self, text: str) -> bool:
        """Safely write text with error handling"""
        try:
            self.logger.debug(f"Writing text: {text}")
            pyautogui.write(text)
            time.sleep(self.config.write_delay)
            return True
        except Exception as e:
            self.logger.error(f"Error writing text '{text}': {e}")
            self.stats['errors'] += 1
            return False
    
    def safe_keyboard_press(self, key: str, presses: int = 1) -> bool:
        """Safely press keys with error handling and random scrolling"""
        try:
            self.press_count += 1
            
            # Random scrolling to prevent detection
            if self.press_count >= self.config.press_count_threshold:
                self.logger.debug("Performing random scroll")
                self._scroll_mouse_randomly()
                time.sleep(self.config.press_delay)
                self.press_count = 0
            
            self.logger.debug(f"Pressing key '{key}' {presses} times")
            for _ in range(presses):
                pyautogui.press(key)
                time.sleep(self.config.press_delay)
            
            return True
        except Exception as e:
            self.logger.error(f"Error pressing key '{key}': {e}")
            self.stats['errors'] += 1
            return False
    
    def safe_hotkey(self, *keys) -> bool:
        """Safely execute hotkey combination"""
        try:
            key_combo = '+'.join(keys)
            self.logger.debug(f"Executing hotkey: {key_combo}")
            pyautogui.hotkey(*keys)
            time.sleep(self.config.hotkey_delay)
            return True
        except Exception as e:
            self.logger.error(f"Error executing hotkey {keys}: {e}")
            self.stats['errors'] += 1
            return False
    
    def safe_click(self, x: int, y: int) -> bool:
        """Safely click at coordinates"""
        try:
            self.logger.debug(f"Clicking at coordinates: ({x}, {y})")
            pyautogui.click(x, y)
            return True
        except Exception as e:
            self.logger.error(f"Error clicking at ({x}, {y}): {e}")
            self.stats['errors'] += 1
            return False
    
    def get_week_dates(self, year: int, week_number: int) -> List[datetime.date]:
        """Get all dates for a given week number"""
        try:
            first_day = datetime.date.fromisocalendar(year, week_number, 1)
            week_days = [first_day + datetime.timedelta(days=i) for i in range(7)]
            self.logger.debug(f"Week {week_number} dates: {week_days[0]} to {week_days[-1]}")
            return week_days
        except Exception as e:
            self.logger.error(f"Error calculating week dates for week {week_number}: {e}")
            return []
    
    def create_new_week_entry(self) -> bool:
        """Create a new week entry"""
        try:
            self.logger.debug("Creating new week entry")
            if not self.safe_hotkey('shift', 'enter'):
                return False
            if not self.safe_keyboard_press('up'):
                return False
            if not self.safe_click(*self.config.click_coordinates):
                return False
            return True
        except Exception as e:
            self.logger.error(f"Error creating new week entry: {e}")
            return False
    
    def process_single_week(self, year: int, week_number: int) -> bool:
        """Process a single week's schedule"""
        try:
            self.logger.info(f"Processing week {week_number} of {year}")
            
            week_days = self.get_week_dates(year, week_number)
            if not week_days:
                return False
            
            # Generate week string
            year_2d = str(year)[-2:]
            start_date = week_days[0]
            end_date = week_days[-1]
            
            start_date_str = f"{start_date.day:02d}{start_date.month:02d}"
            end_date_str = f"{end_date.day:02d}{end_date.month:02d}"
            week_string = f"{year},{week_number:02d}={start_date_str}-{end_date_str} {end_date.month}-{end_date.day}"
            
            # Write week header
            if not self.safe_keyboard_write(week_string):
                return False
            
            # Set medium priority
            if not self.safe_hotkey('alt', '3'):
                return False
            
            # Create new week entry
            if not self.create_new_week_entry():
                return False
            
            time.sleep(1)
            
            # Create daily entries
            for day in week_days:
                day_str = f"{day.day:02d},{day.month:02d},{year_2d} {day.month}-{day.day}"
                if not self.safe_keyboard_write(day_str):
                    continue
                
                # Set low priority
                if not self.safe_hotkey('alt', '2'):
                    continue
                
                if not self.safe_keyboard_press('enter'):
                    continue
                
                if day != week_days[-1]:
                    if not self.safe_keyboard_press('enter'):
                        continue
                
                self.stats['tasks_created'] += 1
            
            """
            # Navigate back up
            if not self.safe_keyboard_press('up', 7):
                return False
            
            # Create time slot entries
            for day in week_days:
                if not self.safe_hotkey('shift', 'enter'):
                    continue
                
                time.sleep(1)
                
                # Create time slot strings
                for i, time_slot in enumerate(self.config.time_slots):
                    
                    #time_str = f"{i}= {day.month}-{day.day} {time_slot}"
                    '''
                    if i < len(self.config.time_slots) - 1:
                        if not self.safe_keyboard_press('enter', 2):
                            continue
                    else:
                        if not self.safe_keyboard_press('enter'):
                            continue
                
                    '''
                    time_str = f"{i}= "
                    if not self.safe_keyboard_write(time_str):
                        continue
                    if i < len(self.config.time_slots) - 1 and not self.safe_keyboard_press('enter'):
                            continue
                     
                if not self.safe_keyboard_press('down'):
                    continue
                
                self.stats['tasks_created'] += 3  # 3 time slots per day
                """
            self.stats['weeks_processed'] += 1
            self.logger.info(f"Successfully processed week {week_number}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error processing week {week_number}: {e}")
            self.stats['errors'] += 1
            return False
    
    def _scroll_mouse_randomly(self):
        """Perform random mouse scrolling"""
        try:
            scroll_amount = random.choice([self.config.scroll_lines, -self.config.scroll_lines])
            pyautogui.scroll(scroll_amount)
            pyautogui.scroll(self.config.max_scroll_down)
            time.sleep(1)
        except Exception as e:
            self.logger.error(f"Error during random scrolling: {e}")
    
    def remove_date_task(self) -> bool:
        """Remove date task (utility function)"""
        try:
            for _ in range(3):
                if not self.safe_hotkey('ctrl', '0'):
                    return False
                time.sleep(2)
                if not self.safe_keyboard_press('down'):
                    return False
            return True
        except Exception as e:
            self.logger.error(f"Error removing date task: {e}")
            return False
    
    def remove_damage(self):
        """Remove damage from tasks"""
        self.logger.info("Starting damage removal process")
        time.sleep(5)
        
        for i in range(7):
            self.logger.debug(f"Processing day {i+1}/7 for damage removal")
            if not self.safe_keyboard_press('down'):
                continue
            if not self.remove_date_task():
                self.logger.warning(f"Failed to remove date task for day {i+1}")
    
    def run_scheduler(self, year: int, start_week: int, end_week: int) -> dict:
        """Main function to run the scheduler"""
        self.stats['start_time'] = datetime.datetime.now()
        self.logger.info(f"Starting scheduler for weeks {start_week}-{end_week} of {year}")
        
        try:
            for week_num in range(start_week, end_week + 1):
                self.logger.info(f"Processing week {week_num}/{end_week}")
                
                # Safety delay
                time.sleep(self.config.safety_delay)
                
                # Enter key to start
                if not self.safe_keyboard_press('enter'):
                    continue
                
                # Process the week
                success = self.process_single_week(year, week_num)
                if not success:
                    self.logger.warning(f"Failed to process week {week_num}")
                
                # Progress update
                progress = ((week_num - start_week + 1) / (end_week - start_week + 1)) * 100
                self.logger.info(f"Progress: {progress:.1f}% complete")
            
            self.stats['end_time'] = datetime.datetime.now()
            self.logger.info("Scheduler completed successfully")
            
        except KeyboardInterrupt:
            self.logger.info("Scheduler interrupted by user")
        except Exception as e:
            self.logger.error(f"Unexpected error in scheduler: {e}")
        finally:
            self._save_stats()
        
        return self.stats
    
    def _save_stats(self):
        """Save execution statistics"""
        try:
            stats_dir = Path("stats")
            stats_dir.mkdir(exist_ok=True)
            
            # Calculate duration
            if self.stats['start_time'] and self.stats['end_time']:
                duration = self.stats['end_time'] - self.stats['start_time']
                self.stats['duration_seconds'] = duration.total_seconds()
                self.stats['duration_formatted'] = str(duration)
            
            # Save to JSON
            stats_file = stats_dir / f"scheduler_stats_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            
            # Convert datetime objects to strings for JSON serialization
            json_stats = self.stats.copy()
            for key, value in json_stats.items():
                if isinstance(value, datetime.datetime):
                    json_stats[key] = value.isoformat()
            
            with open(stats_file, 'w') as f:
                json.dump(json_stats, f, indent=2)
            
            self.logger.info(f"Statistics saved to {stats_file}")
            self._print_summary()
            
        except Exception as e:
            self.logger.error(f"Error saving statistics: {e}")
    
    def _print_summary(self):
        """Print execution summary"""
        print("\n" + "="*50)
        print("EXECUTION SUMMARY")
        print("="*50)
        print(f"Weeks processed: {self.stats['weeks_processed']}")
        print(f"Tasks created: {self.stats['tasks_created']}")
        print(f"Errors encountered: {self.stats['errors']}")
        if 'duration_formatted' in self.stats:
            print(f"Total duration: {self.stats['duration_formatted']}")
        print("="*50)

def load_config(config_file: Optional[str] = None) -> Config:
    """Load configuration from file or use defaults"""
    if config_file and Path(config_file).exists():
        try:
            with open(config_file, 'r') as f:
                config_data = json.load(f)
            return Config(**config_data)
        except Exception as e:
            print(f"Error loading config file: {e}")
            print("Using default configuration")
    
    return Config()

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="Enhanced Week Scheduler Script")
    parser.add_argument("--year", type=int, default=datetime.date.today().year,
                       help="Year to process (default: current year)")
    parser.add_argument("--start-week", type=int, default=1,
                       help="Starting week number (default: 1)")
    parser.add_argument("--end-week", type=int, default=52,
                       help="Ending week number (default: 52)")
    parser.add_argument("--config", type=str, help="Path to configuration file")
    parser.add_argument("--remove-damage", action="store_true",
                       help="Run damage removal instead of scheduler")
    parser.add_argument("--dry-run", action="store_true",
                       help="Simulate execution without actual automation")
    
    args = parser.parse_args()
    
    # Load configuration
    config = load_config(args.config)

    
    # Create scheduler instance
    scheduler = WeekScheduler(config)
    
    if args.dry_run:
        print("DRY RUN MODE - No actual automation will be performed")
        scheduler.logger.info("Running in dry-run mode")
        return
    
    try:
        if args.remove_damage:
            scheduler.logger.info("Running damage removal")
            scheduler.remove_damage()
        else:
            # Validate week range
            if args.start_week > args.end_week:
                print("Error: Start week cannot be greater than end week")
                return
            
            if args.start_week < 1 or args.end_week > 53:
                print("Error: Week numbers must be between 1 and 53")
                return
            
            # Run scheduler
            stats = scheduler.run_scheduler(args.year, args.start_week, args.end_week)
            
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
    except Exception as e:
        print(f"Unexpected error: {e}")
        scheduler.logger.error(f"Unexpected error in main: {e}")

if __name__ == "__main__":
    main()