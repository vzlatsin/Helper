import React from 'react';
import '@testing-library/jest-dom/extend-expect';
import { render, screen, fireEvent } from '@testing-library/react';
import TimeManagement from '../src/components/TimeManagement';

test('renders the input fields and submit button', () => {
    console.log("Running test: renders the input fields and submit button");
    render(<TimeManagement />);
    expect(screen.getByLabelText(/start time/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/end time/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/task description/i)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /submit/i })).toBeInTheDocument();
});

test('submits the form and displays the task', () => {
    console.log("Running test: submits the form and displays the task");
    render(<TimeManagement />);

    fireEvent.change(screen.getByLabelText(/date/i), { target: { value: '2024-06-18' } });
    fireEvent.change(screen.getByLabelText(/start time/i), { target: { value: '09:00' } });
    fireEvent.change(screen.getByLabelText(/end time/i), { target: { value: '10:00' } });
    fireEvent.change(screen.getByLabelText(/task description/i), { target: { value: 'Testing task submission' } });

    fireEvent.click(screen.getByRole('button', { name: /submit/i }));

    expect(screen.getByText(/2024-06-18 - 09:00 to 10:00: Testing task submission/i)).toBeInTheDocument();
});

test('allows submission with empty start and end times', () => {
    render(<TimeManagement />);

    fireEvent.change(screen.getByLabelText(/date/i), { target: { value: '2024-06-18' } });
    fireEvent.change(screen.getByLabelText(/task description/i), { target: { value: 'Test Task' } });

    fireEvent.click(screen.getByRole('button', { name: /submit/i }));

    expect(screen.queryByText(/Both start time and end time must be provided/)).not.toBeInTheDocument();
    expect(screen.queryByText(/Invalid time format/)).not.toBeInTheDocument();
    expect(screen.queryByText(/End time must be after start time/)).not.toBeInTheDocument();
    expect(screen.getByText(/2024-06-18 - 00:00 to 00:00: Test Task/)).toBeInTheDocument();
});

test('shows error if only one of start or end time is provided', () => {
    render(<TimeManagement />);

    fireEvent.change(screen.getByLabelText(/date/i), { target: { value: '2024-06-18' } });
    fireEvent.change(screen.getByLabelText(/start time/i), { target: { value: '09:00' } });
    fireEvent.change(screen.getByLabelText(/task description/i), { target: { value: 'Test Task' } });

    fireEvent.click(screen.getByRole('button', { name: /submit/i }));

    expect(screen.getByText(/Both start time and end time must be provided/)).toBeInTheDocument();
});

test('shows error if end time is not after start time', () => {
    render(<TimeManagement />);

    fireEvent.change(screen.getByLabelText(/date/i), { target: { value: '2024-06-18' } });
    fireEvent.change(screen.getByLabelText(/start time/i), { target: { value: '09:00' } });
    fireEvent.change(screen.getByLabelText(/end time/i), { target: { value: '08:00' } });
    fireEvent.change(screen.getByLabelText(/task description/i), { target: { value: 'Test Task' } });

    fireEvent.click(screen.getByRole('button', { name: /submit/i }));

    expect(screen.getByText(/End time must be after start time/)).toBeInTheDocument();
});
