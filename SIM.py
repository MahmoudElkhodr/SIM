import random
import time
import json
import hashlib
import matplotlib.pyplot as plt
import numpy as np

# Function to generate random sensor data for heart rate, blood pressure, and temperature
def generate_sensor_data(num_readings):
    data = []
    for _ in range(num_readings):
        # Simulate heart rate, blood pressure, and temperature readings
        heart_rate = random.randint(55, 120)  # 60-100 bpm is normal, above 100 is elevated
        blood_pressure_systolic = random.randint(85, 140)  # 90-120 mmHg systolic is normal
        blood_pressure_diastolic = random.randint(55, 90)  # 60-80 mmHg diastolic is normal
        temperature = round(random.uniform(36.0, 39.0), 1)  # 36.5-37.5°C is normal, above is elevated
        data.append({"heart_rate": heart_rate, "blood_pressure": (blood_pressure_systolic, blood_pressure_diastolic), "temperature": temperature})
    return data

# Function to annotate sensor data with semantic labels
def annotate_sensor_data(sensor_data):
    annotated_data = []
    for reading in sensor_data:
        # Annotate heart rate, blood pressure, and temperature
        heart_rate_status = "Normal" if reading["heart_rate"] <= 100 else "Elevated"
        bp_status = "Normal" if 90 <= reading["blood_pressure"][0] <= 120 else "Elevated or Low"
        temp_status = "Normal" if 36.5 <= reading["temperature"] <= 37.5 else "Elevated or Low"
        annotated_data.append({
            "heart_rate": reading["heart_rate"],
            "heart_rate_status": heart_rate_status,
            "blood_pressure": reading["blood_pressure"],
            "blood_pressure_status": bp_status,
            "temperature": reading["temperature"],
            "temperature_status": temp_status
        })
    return annotated_data

# Function to simulate encryption using SHA-256 hash
def encrypt_data(data):
    data_string = json.dumps(data).encode()
    hash_object = hashlib.sha256(data_string)
    return hash_object.hexdigest()

# Function to simulate smart contract execution
def execute_smart_contract(encrypted_data):
    if 'a' in encrypted_data:  # Placeholder condition
        print("Smart Contract: Alert sent to healthcare provider.")
    else:
        print("Smart Contract: No action needed.")

# Function to query and analyze data
def query_and_analyze_data(annotated_data, metric, condition):
    results = [data for data in annotated_data if data[metric] == condition]
    continuous_elevated = all(data[metric] == condition for data in results)
    return continuous_elevated

# Function to simulate triggering services
def trigger_services(risk_detected):
    if risk_detected:
        print("Alert: Sending notification to emergency response team.")
        print("Action: Sending health advisory to user's health monitoring app.")

# Function to simulate AI feedback and analysis module
def ai_feedback_and_analysis(feedback):
    global consider_exercise_context
    consider_exercise_context = feedback.get('consider_exercise_context', False)
    print(f"AI Feedback Processed: Consider exercise context - {consider_exercise_context}")

# Function to annotate sensor data considering exercise context
def annotate_sensor_data_with_context(sensor_data):
    annotated_data = []
    for reading in sensor_data:
        heart_rate = reading["heart_rate"]
        heart_rate_status = "Normal (Exercise)" if heart_rate <= 120 and consider_exercise_context else "Normal" if heart_rate <= 100 else "Elevated"
        annotated_data.append({"heart_rate": heart_rate, "heart_rate_status": heart_rate_status})
    return annotated_data

# Main execution flow
sensor_data = generate_sensor_data(10)
annotated_sensor_data = annotate_sensor_data(sensor_data)
encrypted_sensor_data = [encrypt_data(reading) for reading in annotated_sensor_data]

# Time measurement for encryption
start_encryption_time = time.time()
encrypted_sensor_data = [encrypt_data(reading) for reading in annotated_sensor_data]
end_encryption_time = time.time()
encryption_time = (end_encryption_time - start_encryption_time) * 1000  # Convert to milliseconds

# Time measurement for smart contract execution
start_time = time.time()
for encrypted_reading in encrypted_sensor_data:
    execute_smart_contract(encrypted_reading)
end_time = time.time()
smart_contract_time = (end_time - start_time) * 1000  # Convert to milliseconds

# AI Feedback and Context-Aware Annotation
consider_exercise_context = False
ai_feedback_and_analysis({"consider_exercise_context": True})
annotated_sensor_data_context = annotate_sensor_data_with_context(sensor_data)

# Trigger services based on data analysis
risk_detected_hr = query_and_analyze_data(annotated_sensor_data, 'heart_rate_status', 'Elevated')
risk_detected_bp = query_and_analyze_data(annotated_sensor_data, 'blood_pressure_status', 'Elevated')
risk_detected_temp = query_and_analyze_data(annotated_sensor_data, 'temperature_status', 'Elevated')
trigger_services(risk_detected_hr or risk_detected_bp or risk_detected_temp)


def healthcare_provider_review(annotated_data):
    # Simulate a healthcare provider reviewing the data and providing feedback
    for reading in annotated_data:
        if reading['heart_rate_status'] == 'Elevated':
            print(f"Reviewing elevated heart rate data: {reading}")
            # Simulate provider tagging the reading as a false alarm due to exercise
            feedback = {"consider_exercise_context": True}
            ai_feedback_and_analysis(feedback)
            print("Healthcare provider adjusted the context based on exercise.")



def patient_confirm_activity(annotated_data, activity):
    # Simulate a patient confirming they were exercising during elevated readings
    for reading in annotated_data:
        if reading['heart_rate_status'] == 'Elevated':
            print(f"Patient confirms {activity} during elevated heart rate.")
            feedback = {"consider_exercise_context": True}
            ai_feedback_and_analysis(feedback)
            print("System updated to consider exercise context.")








# Visualization
# Plotting heart rate distribution
heart_rates = [reading["heart_rate"] for reading in sensor_data]
plt.hist(heart_rates, bins=10, color='blue', alpha=0.7)
plt.title('Distribution of Heart Rate Readings')
plt.xlabel('Heart Rate (bpm)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


def count_annotations(data, key):
    counts = {}
    for item in data:
        label = item[key]
        if label in counts:
            counts[label] += 1
        else:
            counts[label] = 1
    return counts
# Plotting annotation categorization
annotation_counts = count_annotations(annotated_sensor_data_context, 'heart_rate_status')
labels = list(annotation_counts.keys())
values = list(annotation_counts.values())
plt.bar(labels, values)
plt.xlabel('Annotation Labels')
plt.ylabel('Count')
plt.title('Annotation Categorization Chart')
plt.show()

# Plotting before and after feedback comparison
before_counts = count_annotations(annotated_sensor_data, 'heart_rate_status')
after_counts = count_annotations(annotated_sensor_data_context, 'heart_rate_status')
x = np.arange(len(before_counts))  # label locations
width = 0.35  # width of the bars
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, list(before_counts.values()), width, label='Before Feedback')
rects2 = ax.bar(x + width/2, list(after_counts.values()), width, label='After Feedback')
ax.set_xlabel('Annotation Labels')
ax.set_ylabel('Count')
ax.set_title('Feedback Impact on Annotations')
ax.set_xticks(x)
ax.set_xticklabels(list(before_counts.keys()))
ax.legend()
fig.tight_layout()
plt.show()

# Plotting encryption and smart contract execution times
processes = ['Encryption', 'Smart Contract Execution']
times = [encryption_time, smart_contract_time]
plt.bar(processes, times, color=['blue', 'orange'])
plt.xlabel('Process')
plt.ylabel('Time (milliseconds)')
plt.title('Time Taken for Encryption and Smart Contract Execution (ms)')
plt.show()
