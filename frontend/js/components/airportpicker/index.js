/*
 * © 2017 Tal Globus. All Rights Reserved.
 */

import styles from './styles';
import React, { Component } from 'react';
import { View, Text, Picker, StyleSheet } from 'react-native';

import airports from './sorted';

class AirportPicker extends Component {
	constructor(props) {
		super(props);
		this.state = {airport: 'Barcelona International Airport, Barcelona, ES'};

		this.updateUser = (airport) => {
			this.setState({ airport: airport });

		};
	}

	render() {
		return (
			<View>
				<Picker style={styles.Picker} itemStyle={styles.item} mode="dropdown" selectedValue = {this.state.airport}
						onValueChange = {this.updateUser}>
					{airports.map(({name, city, country, code}) =>
						// <th key={title}>{title}</th>
						<Picker.Item label={name} value={`${name}, ${city}, ${country}`}
									 key={`${name}, ${city}, ${country}`} />
					)}
				</Picker>
				<Text style = {styles.text}>{this.state.airport}</Text>
			</View>
		)
	}
}

// const styles = StyleSheet.create({
// 	text: {
// 		fontSize: 30,
// 		alignSelf: 'center',
// 		color: 'red'
// 	}
// });

export default AirportPicker;