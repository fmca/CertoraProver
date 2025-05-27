/*
 *     The Certora Prover
 *     Copyright (C) 2025  Certora Ltd.
 *
 *     This program is free software: you can redistribute it and/or modify
 *     it under the terms of the GNU General Public License as published by
 *     the Free Software Foundation, version 3 of the License.
 *
 *     This program is distributed in the hope that it will be useful,
 *     but WITHOUT ANY WARRANTY; without even the implied warranty of
 *     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *     GNU General Public License for more details.
 *
 *     You should have received a copy of the GNU General Public License
 *     along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

package config

import log.*
import org.apache.commons.cli.Option

/**
 * A registrar for configuration.
 * Current main use is to process all [CmdLine] options transparently in [ArgsParser]
 */
object ConfigRegister {

    val registeredConfigs = mutableSetOf<ConfigType<*>>()
    fun register(configType: ConfigType<*>) {
        // checks
        val cliOpts = mutableSetOf<String>()
            .also { it.addAll(getCLIOptions().mapNotNull { it.opt }) }
            .also { it.addAll(getCLIOptions().mapNotNull { it.longOpt }) }
        when (configType) {
            is ConfigType.CmdLine -> {
                check(configType.option.realOpt() !in cliOpts) { "Option ${configType.option.realOpt()} already registered" }
                check( configType.option.longOpt == null) { "Option ${configType.option.opt} has a long option too ${configType.option.longOpt}, which we do not use (use aliases instead)"}
            }
            else -> Unit
        }

        // register
        registeredConfigs.add(configType)
    }

    fun getCLIOptions(): List<Option> {
        return registeredConfigs.mapNotNull { if (it is ConfigType.CmdLine) it.allOptions else null }.flatten()
    }
}
